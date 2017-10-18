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

    def get_participants(self):
        builder_list = []
        for player in self.get_others_in_group():
            builder_list.append(player.participant.id_in_session)

        return builder_list

    q2_communication_surprised = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_satisfied = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_communication_upset = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_best_player = models.CharField(
        max_length=255,  widget=widgets.RadioSelect(),
        choices=get_participants())

    q2_recomendation_for_actions = models.TextField()
    q2_communication_helped_positive_and_negative = models.TextField()

    q2_opinion_recomendation_everyone = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_opinion_recomendation_fair = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_opinion_recomendation_max_resources = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_opinion_recomendation_understandable = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_pressure_behaving_like_settled_rules = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_would_it_disturb_you_behaving_differently = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_is_there_any_kind_of_social_pressure = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_i_will_follwow_the_recommendation_entirely = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_i_will_follwow_the_recommendation_maximizing_my_advantage = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_others_follow_the_recommendations_entirely = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_others_follow_the_recommendations_try_to_max_their_advantage = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))

    q2_how_much_cooperate_because_communication = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_team_spirit = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_importance_of_your_image = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_importance_maximum_resources_to_everyone = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_importance_other_members_trust_in_you = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_importance_maximum_resources_to_everyone_not_you = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_how_much_trust_do_you_have_into_other_members = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_how_much_do_you_like_the_other_team_members = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_how_good_you_understand_solving_problem_max_resources = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_afterc_others_understand_solving_problem_great_max_resources = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_which_strategy_would_you_follow_and_why = models.TextField()

