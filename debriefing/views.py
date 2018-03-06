# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class PlaceboDebriefing(Page):

    form_model = models.Player
    form_fields = [

        'debriefing_guess_which_group',
        'debriefing_sure_about_confidant_in_group',
        'debriefing_who_was_confidant',
        'what_made_you_assume_confidant',
        'debriefing_feedback'
    ]

    def debriefing_who_was_confidant_choices(self):

        choices = []
        for player in self.group.get_players():

            if player.id_in_group == self.player.id_in_group:
                choices.append('Ich')
            else:
                choices.append('Spieler ' + str(player.id_in_group))

        choices.append('Niemand (Gruppe ohne Konfident)')

        return choices

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get(
                'is_negative_confidant', False):
            return False

        return True


class ConfidantDebriefing(Page):

    form_model = models.Player
    form_fields = [

        'confidant_debriefing_feedback'
    ]

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get(
                'is_negative_confidant', False):
            return True

        return False


page_sequence = [
    PlaceboDebriefing, ConfidantDebriefing
]
