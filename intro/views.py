# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1
    def vars_for_template(self):
        return {"players_per_group": 3 }#self.session.config['players_per_group']}



class Agreement(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1


page_sequence = [
    Instructions, Agreement
]
