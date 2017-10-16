# -*- coding: utf-8 -*-
from __future__ import division

import csv
import datetime

from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.template import loader
from django.forms.models import model_to_dict
from django.utils.six.moves import range
from django.http import HttpResponse, StreamingHttpResponse

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

import dateutil.parser


MESSAGES_TPL = loader.get_template("chat/messages.html")


# =============================================================================
# PAGES
# =============================================================================

class SmallTalk(Page):
    template_name = 'chat/placebo_instructions.html'
    # def is_displayed(self):
    #     return self.player.group.treatment  == Constants.treatment_small_talk


class ChatWaitPage(WaitPage):
    pass


class Chat(Page):
    pass

page_sequence = [
    SmallTalk,
    ChatWaitPage,
    Chat,
]

# =============================================================================
# CHAT WEB SOCKET
# =============================================================================

@require_GET
def retrieve_messages(request):
    MESSAGES_TPL = loader.get_template("chat/messages.html")
    group_id = int(request.GET["group"])
    last_message = request.GET["last_message"] or None

    messages = models.Message.objects.filter(group__id=group_id)

    if last_message:
        last_message = dateutil.parser.parse(last_message)
        messages = messages.filter(
            timestamp__gt=last_message
        ).order_by("timestamp")[:10].select_related()
    else:
        messages = messages.order_by("timestamp").select_related()

    messages = list(messages)

    if messages:
        message_html = MESSAGES_TPL.render({"messages": messages})
        last_message = messages[-1].timestamp.isoformat()
        response = {
            "hasMessages": True,
            "messagesHTML": message_html,
            "lastMessage": last_message}
    else:
        response = {"hasMessages": False}
    return JsonResponse(response)

@require_POST
def send_message(request):
    group_id = int(request.POST["group"])
    player_id = int(request.POST["player"])
    message_txt = request.POST["message"]

    message = models.Message.objects.create(
        group_id=group_id, player_id=player_id, message=message_txt)

    response = JsonResponse({'message': message.id})
    return response


@require_GET
def export(request):
    class Echo(object):
        def write(self, value):
            return value

    header = [
        "Participant.id_in_session",
        "Participant.code",
        "Participant.label",
        "Participant._is_bot",
        "Participant._index_in_pages",
        "Participant._max_page_index",
        "Participant._current_app_name",
        "Participant._round_number",
        "Participant._current_page_name",
        "Participant.ip_address",
        "Participant.time_started",
        "Participant.exclude_from_data_analysis",
        "Participant.visited",
        "Participant.mturk_worker_id",
        "Participant.mturk_assignment_id",

        "Player.id_in_group",
        "Group.id_in_subsession",

        "Subsession.round_number",

        "Session.code",
        "Session.label",
        "Session.experimenter_name",
        "Session.time_scheduled",
        "Session.time_started",
        "Session.comment",
        "Session.is_demo",

        "Message.message",
        "Message.timestamp",
    ]

    def iter_rows():
        yield header
        for msg in models.Message.objects.all().order_by("timestamp"):
            player = msg.player
            participant = player.participant
            group = msg.group
            subsession = group.subsession
            session = subsession.session

            row = [
                 participant.id_in_session,
                 participant.code,
                 participant.label,
                 participant._is_bot,
                 participant._index_in_pages,
                 participant._max_page_index,
                 participant._current_app_name,
                 participant._round_number,
                 participant._current_page_name,
                 participant.ip_address,
                 participant.time_started,
                 participant.exclude_from_data_analysis,
                 participant.visited,
                 participant.mturk_worker_id,
                 participant.mturk_assignment_id,

                 player.id_in_group,
                 group.id_in_subsession,

                 subsession.round_number,

                 session.code,
                 session.label,
                 session.experimenter_name,
                 session.time_scheduled,
                 session.time_started,
                 session.comment,
                 session.is_demo,

                 msg.message,
                 msg.timestamp.isoformat(),
            ]
            yield row

    rows = iter_rows()
    now = datetime.date.today().isoformat()

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in rows),
                                     content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="chat_messages (accesed {}).csv"'.format(now)
    return response


