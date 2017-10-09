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

        'q2_recomendation_for_actions', 'q2_communication_helped_positive_and_negative',
        'q2_opinion_recomendation_everyone', 'q2_opinion_recomendation_fair', 'q2_opinion_recomendation_max_resources', 'q2_opinion_recomendation_understandable',

        'q2_pressure_behaving_like_settled_rules',
        'q2_would_it_disturb_you_behaving_differently',
        'q2_is_there_any_kind_of_social_pressure',

        'q2_i_will_follwow_the_recommendation_entirely', 'q2_i_will_follwow_the_recommendation_maximizing_my_advantage',
        'q2_others_follow_the_recommendations_entirely', 'q2_others_follow_the_recommendations_try_to_max_their_advantage',

        'q2_how_much_cooperate_because_communication',
        'q2_team_spirit',

        'q2_afterc_importance_of_your_image',
        'q2_afterc_importance_maximum_resources_to_everyone',
        'q2_afterc_importance_other_members_trust_in_you',
        'q2_afterc_importance_maximum_resources_to_everyone_not_you',
        'q2_afterc_how_much_trust_do_you_have_into_other_members',
        'q2_afterc_how_much_do_you_like_the_other_team_members',
        'q2_afterc_how_good_you_understand_solving_problem_max_resources',
        'q2_afterc_others_understand_solving_problem_great_max_resources',

        'q2_which_strategy_would_you_follow_and_why'
    ]


page_sequence = [
    Questionnaire2
]
