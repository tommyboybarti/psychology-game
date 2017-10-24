# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire2(Page):

    form_model = models.Player
    form_fields = [

        'q2_communication_surprised', 'q2_communication_satisfied', 'q2_communication_upset',
        'q2_how_did_you_talk_about_the_cleaning',

        'form.q2_communication_fair_discussion',
        'form.q2_communication_fear_criticism',
        'form.q2_communication_to_be_right',
        'form.q2_communication_give_opinion',
        'form.q2_communication_others_opinions',
        'form.q2_communication_whine',
        'form.q2_communication_inputs',
        'q2_best_player'
    ]


page_sequence = [
    Questionnaire2
]
