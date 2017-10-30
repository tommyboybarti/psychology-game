# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class ConfidantQ3(Page):
    form_model = models.Player
    form_fields = [

        'q3_confidant_second_game_teamwork',
        'q3_confidant_second_game_teamspirit',
        'q3_confidant_majority_followed_communication_inputs',
        'q3_confidant_majority_took_advantage_communication_inputs',
        'q3_confidant_minority_followed_communication_inputs',
        'q3_confidant_minority_took_advantage_communication_inputs',
        'q3_confidant_best_strategy_to_max_resources',
        'q3_confidant_gender',
        'q3_confidant_birthday',
        'q3_confidant_main_subject_in_university',
        'q3_confidant_already_take_part_in_a_problem_solving',
        'q3_confidant_already_took_part_x_times_for_x_months',
        'q3_confidant_experiment_itself_was_interessting',
        'q3_confidant_were_you_personally_engaged_achieving_good_results',
        'q3_confidant_dificult_understanding_and_solving_the_problem',
        'q3_confidant_was_it_obvious_what_to_do',
        'q3_confidant_count_unclear_questions',
        'q3_confidant_unclear_questions_description',
        'q3_confidant_technical_issues',
        'q3_confidant_technical_issues_details'
    ]

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get(
                'is_negative_confidant', False):
            return True

        return False


class PlaceboQ3(Page):
    form_model = models.Player
    form_fields = [

        'q3_second_game_results_surprised',
        'q3_second_game_results_satisfied',
        'q3_second_game_results_upset',
        'q3_second_game_teamwork',
        'q3_second_game_teamspirit',
        'q3_communication_inputs_maxresources_how_useful',
        'q3_followed_communication_inputs',
        'q3_took_advantage_communication_inputs',
        'q3_majority_followed_communication_inputs',
        'q3_majority_took_advantage_communication_inputs',
        'q3_minority_followed_communication_inputs',
        'q3_minority_took_advantage_communication_inputs',
        'q3_how_max_resources_communication_inputs_if_followed',
        'q3_after_second_round_like_others',
        'q3_second_round_impressions',
        'q3_best_strategy_to_max_resources',
        'q3_gender',
        'q3_birthday',
        'q3_main_subject_in_university',
        'q3_already_take_part_in_a_problem_solving',
        'q3_already_took_part_x_times_for_x_months',
        'q3_experiment_itself_was_interessting',
        'q3_were_you_personally_engaged_achieving_good_results',
        'q3_dificult_understanding_and_solving_the_problem',
        'q3_was_it_obvious_what_to_do',
        'q3_count_unclear_questions',
        'q3_unclear_questions_description',
        'q3_technical_issues',
        'q3_technical_issues_details',
        'q3_opinion_about_questions_and_hypotheses'
    ]

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get(
                'is_negative_confidant', False):
            return False

        return True


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


page_sequence = [
    ConfidantQ3, PlaceboQ3, PlaceboDebriefing
]
