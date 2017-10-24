# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import random

import otree.models
from otree.db import models
from otree import widgets
from otree.common import Currency as c, currency_range, safe_json
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer
# </standard imports>

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'toilet_questionnaire_2'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    def __init__(self):
        self.q2_best_player = models.CharField(
            max_length=255, widget=widgets.RadioSelect(),
            choices = self.get_choices(self.get_participants()))

    def get_participants(self):
        builder_list = []
        for player in self.get_others_in_group():
            builder_list.append(player.participant.id_in_session)

        return builder_list

    def get_choices(self, participants):
        choices = []
        choices.append(self)
        for participant in participants:
            choices.append(participant)

        return choices

    q2_communication_surprised = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_satisfied = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_upset = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_communication_fair_discussion = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_fear_cirticism = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_to_be_right = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_communication_give_opinion = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_others_opinions = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_whine = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_inputs = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_best_player = models.CharField(
        max_length=255,  widget=widgets.RadioSelect(),
        choices = [])