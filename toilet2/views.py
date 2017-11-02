# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class InitGroup(WaitPage):

    def after_all_players_arrive(self):
        self.group.init_group()


class Choice(Page):

    template_name = "toilet/Choice.html"

    form_model = models.Player
    form_fields = ['use_toilet', 'small_cleaning', 'big_clean']
    timeout_seconds = None
    timeout_submission = {'use_toilet': True,
                          'small_cleaning': False,
                          'big_clean': False}


    def is_displayed(self):
        return bool(self.player.health and self.player.health > 0)


class ChoiceWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoff()


class Results(Page):
    template_name = "toilet/Results.html"


page_sequence = [
    InitGroup, Choice, ChoiceWaitPage, Results

]
