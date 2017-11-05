# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1





class Agreement(Page):

    form_model = models.Player
    form_fields = [

        'participant_email'
    ]

    def is_displayed(self):
        return self.subsession.round_number == 1

    def before_next_page(self):
        self.participant.label = self.player.participant_email


page_sequence = [
    Instructions, Agreement
]
