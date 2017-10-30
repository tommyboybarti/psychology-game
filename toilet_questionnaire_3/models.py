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
    q3_second_game_results_surprised = models.PositiveIntegerField(min=1, max=10,
                                                                   widget=widgets.SliderInput(show_value=False))
    q3_second_game_results_satisfied = models.PositiveIntegerField(min=1, max=10,
                                                                   widget=widgets.SliderInput(show_value=False))
    q3_second_game_results_upset = models.PositiveIntegerField(min=1, max=10,
                                                               widget=widgets.SliderInput(show_value=False))

    q3_second_game_teamwork = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q3_second_game_teamspirit = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q3_communication_inputs_maxresources_how_useful = models.PositiveIntegerField(min=1, max=10,
                                                                                  widget=widgets.SliderInput(
                                                                                      show_value=False))
    q3_followed_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                   widget=widgets.SliderInput(show_value=False))
    q3_took_advantage_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                         widget=widgets.SliderInput(show_value=False))
    q3_majority_followed_communication_inputs = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(
        show_value=False))
    q3_majority_took_advantage_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                  widget=widgets.SliderInput(
                                                                                      show_value=False))
    q3_minority_followed_communication_inputs = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(
        show_value=False))
    q3_minority_took_advantage_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                  widget=widgets.SliderInput(
                                                                                      show_value=False))
    q3_how_max_resources_communication_inputs_if_followed = models.PositiveIntegerField(min=1, max=10,
                                                                                        widget=widgets.SliderInput(
                                                                                            show_value=False))
    q3_after_second_round_like_others = models.PositiveIntegerField(min=1, max=10,
                                                                    widget=widgets.SliderInput(show_value=False))
    q3_second_round_impressions = models.TextField()
    q3_best_strategy_to_max_resources = models.TextField()
    q3_gender = models.CharField(choices=["M", "F"], widget=widgets.RadioSelectHorizontal())
    q3_birthday = models.DateField(widget=widgets.Input())
    q3_main_subject_in_university = models.TextField()
    q3_already_take_part_in_a_problem_solving = models.CharField(max_length=255, widget=widgets.RadioSelect(),
                                                                 choices=['Ja', 'Nein'])
    q3_already_took_part_x_times_for_x_months = models.TextField(default='X Male und das letzte Mal vor X Monaten.')
    q3_experiment_itself_was_interessting = models.PositiveIntegerField(min=1, max=10,
                                                                        widget=widgets.SliderInput(show_value=False))
    q3_were_you_personally_engaged_achieving_good_results = models.PositiveIntegerField(min=1, max=10,
                                                                                        widget=widgets.SliderInput(
                                                                                            show_value=False))
    q3_dificult_understanding_and_solving_the_problem = models.PositiveIntegerField(min=1, max=10,
                                                                                    widget=widgets.SliderInput(
                                                                                        show_value=False))
    q3_was_it_obvious_what_to_do = models.PositiveIntegerField(min=1, max=10,
                                                               widget=widgets.SliderInput(show_value=False))
    q3_count_unclear_questions = models.TextField()
    q3_unclear_questions_description = models.TextField()
    q3_technical_issues = models.CharField(max_length=255, widget=widgets.RadioSelect(), choices=['Ja', 'Nein'])
    q3_technical_issues_details = models.TextField()
    q3_opinion_about_questions_and_hypotheses = models.TextField()

    # confidant

    q3_confidant_second_game_teamwork = models.PositiveIntegerField(min=1, max=10,
                                                                    widget=widgets.SliderInput(show_value=False))
    q3_confidant_second_game_teamspirit = models.PositiveIntegerField(min=1, max=10,
                                                                      widget=widgets.SliderInput(show_value=False))
    q3_confidant_majority_followed_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                      widget=widgets.SliderInput(
                                                                                          show_value=False))
    q3_confidant_majority_took_advantage_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                            widget=widgets.SliderInput(
                                                                                                show_value=False))
    q3_confidant_minority_followed_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                      widget=widgets.SliderInput(
                                                                                          show_value=False))
    q3_confidant_minority_took_advantage_communication_inputs = models.PositiveIntegerField(min=1, max=10,
                                                                                            widget=widgets.SliderInput(
                                                                                                show_value=False))
    q3_confidant_best_strategy_to_max_resources = models.TextField()
    q3_confidant_gender = models.CharField(choices=["M", "F"], widget=widgets.RadioSelectHorizontal())
    q3_confidant_birthday = models.DateField(widget=widgets.Input())
    q3_confidant_main_subject_in_university = models.TextField()
    q3_confidant_already_take_part_in_a_problem_solving = models.CharField(max_length=255, widget=widgets.RadioSelect(),
                                                                           choices=['Ja', 'Nein'])
    q3_confidant_already_took_part_x_times_for_x_months = models.TextField(
        default='X Male und das letzte Mal vor X Monaten.')
    q3_confidant_experiment_itself_was_interessting = models.PositiveIntegerField(min=1, max=10,
                                                                                  widget=widgets.SliderInput(
                                                                                      show_value=False))
    q3_confidant_were_you_personally_engaged_achieving_good_results = models.PositiveIntegerField(min=1, max=10,
                                                                                                  widget=widgets.SliderInput(
                                                                                                      show_value=False))
    q3_confidant_dificult_understanding_and_solving_the_problem = models.PositiveIntegerField(min=1, max=10,
                                                                                              widget=widgets.SliderInput(
                                                                                                  show_value=False))
    q3_confidant_was_it_obvious_what_to_do = models.PositiveIntegerField(min=1, max=10,
                                                                         widget=widgets.SliderInput(show_value=False))
    q3_confidant_count_unclear_questions = models.TextField()
    q3_confidant_unclear_questions_description = models.TextField()
    q3_confidant_technical_issues = models.CharField(max_length=255, widget=widgets.RadioSelect(),
                                                     choices=['Ja', 'Nein'])
    q3_confidant_technical_issues_details = models.TextField()


    # debriefing
    debriefing_guess_which_group = models.CharField(max_length=255, widget=widgets.RadioSelect(), choices=[
        'Gruppe mit Anweisungen für alle zu positiver Kommunikation',
        'Gruppe mit Konfident mit positiver Kommunikation',
        'Gruppe mit Konfident mit negativer Kommunikation', 'Kontrollgruppe ohne eigentliche Anweisungen', 'Weiss nicht'
    ])

    debriefing_sure_about_confidant_in_group = models.PositiveIntegerField(min=1, max=10,
                                                                         widget=widgets.SliderInput(show_value=False))

    debriefing_who_was_confidant = models.CharField(max_length=255, widget=widgets.RadioSelect(),
                                                     choices=[])

    what_made_you_assume_confidant = models.TextField(default='n/a')
    debriefing_feedback = models.TextField()
