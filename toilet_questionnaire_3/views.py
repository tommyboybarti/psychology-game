# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire3(Page):

    form_model = models.Player
    form_fields = [
        'q3_second_game_surprised', 'q3_second_game_satisfied', 'q3_second_game_upset',

        'q3_help_each_other_in_the_second_game',
        'q3_team_spirit',
        'q3_recommendations_of_actions_to_maximize_everyones_resources',
        'q3_i_follow_recommendations_of_action_followed', 'q3_i_follow_recommendations_of_action_my_advantage',
        'q3_others_follow_recommendations_of_action_followed', 'q3_others_follow_recommendations_of_action_their_advantage',
        'q3_yopinion_if_they_followed_would_everyone_max_his_resources',

        'q3_second_game_different_and_is_it_because_of_the_communication',
        'q3_the_best_strategy_to_optimize_everyones_resources',

        'q3_gender', 'q3_birthday',
        'q3_main_subject_in_university', 'q3_already_take_part_in_a_problem_solving',

        'q3_experiment_itself_was_interessting',
        'q3_were_you_personally_engaged_achieving_good_results',
        'q3_dificult_understanding_and_solving_the_problem',
        'q3_was_it_obvious_what_to_do',
        'q3_short_feedback'
    ]


page_sequence = [
    Questionnaire3
]
