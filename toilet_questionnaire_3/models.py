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
    name_in_url = 'toilet_questionnaire_3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q3_second_game_surprised = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_second_game_satisfied = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_second_game_upset = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q3_help_each_other_in_the_second_game = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_team_spirit = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_recommendations_of_actions_to_maximize_everyones_resources = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q3_i_follow_recommendations_of_action_followed = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_i_follow_recommendations_of_action_my_advantage = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q3_others_follow_recommendations_of_action_followed = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_others_follow_recommendations_of_action_their_advantage = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q3_yopinion_if_they_followed_would_everyone_max_his_resources = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q3_second_game_different_and_is_it_because_of_the_communication = models.TextField()
    q3_the_best_strategy_to_optimize_everyones_resources = models.TextField()

    q3_gender = models.CharField(choices=["Male", "Female"], widget=widgets.RadioSelectHorizontal())
    q3_birthday = models.DateField(widget=widgets.Input())

    q3_main_subject_in_university = models.TextField()
    q3_already_take_part_in_a_problem_solving = models.BooleanField(widget=widgets.RadioSelectHorizontal())

    q3_experiment_itself_was_interessting = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_were_you_personally_engaged_achieving_good_results = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_dificult_understanding_and_solving_the_problem = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_was_it_obvious_what_to_do = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q3_short_feedback = models.TextField()





