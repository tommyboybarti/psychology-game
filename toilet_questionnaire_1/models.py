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

from django.utils.translation import ugettext as _

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'toilet_questionnaire_1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q1_first_game_judge_surprised = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_first_game_judge_satisfied = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_first_game_judge_upset = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q1_players_helping_each_other = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_team_spirit_or_cohesion = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_important_presented_image_of_and_to_yourself = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_important_maximum_and_fair_resources_to_everyone = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_important_other_members_trust_in_you = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_important_not_you_maximum_and_fair_resources_to_everyone = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_trust_do_you_have_into_other_members = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_how_much_do_you_like_the_other_team_members = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_how_good_do_you_understand_solving = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q1_how_good_do_the_other_group_members_understand_solving = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q1_how_to_improve_the_groups_behavior_to_maximize_resources = models.TextField()
    q1_if_communicate_what_would_you_say_and_why = models.TextField()