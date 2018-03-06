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

    available_group_sizes = (3, 4, 5)


class Subsession(BaseSubsession):

    def chunk_it(self, seq, num):
        avg = len(seq) / float(num)
        out = []
        last = 0.0
        while last < len(seq):
            out.append(seq[int(last):int(last + avg)])
            last += avg
        return sorted(out, key=lambda r: [p.id_in_group for p in r])

    def before_session_starts(self):
        # make groups
        players_per_group = self.session.config['players_per_group']
        players = self.get_players()
        if players_per_group not in Constants.available_group_sizes:
            raise ValueError("'players_per_group' mus be one of {}".format(Constants.available_group_sizes))
        if len(players) % players_per_group != 0:
            raise ValueError("'participants' must be a multiply of {}".format(players_per_group))
        groups_n = int(len(players) / float(players_per_group))
        groups_mtx = self.chunk_it(players, groups_n)
        self.set_group_matrix(groups_mtx)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    q2_communication_surprised = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_satisfied = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_upset = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_fair_discussion = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_fear_criticism = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_to_be_right = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_give_opinion = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_others_opinions = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_whine = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_inputs_considered = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_best_player = models.CharField(max_length=255, widget=widgets.RadioSelect(),choices=[])
    q2_communication_focused = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_efficient = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_communication_interested_in_solution = models.PositiveIntegerField(min=1, max=5, widget=widgets.SliderInput(show_value=False))
    q2_discussion_tense = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_discussion_tense_why = models.TextField()
    q2_chat_instructions_helpful = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_chat_instructions_followed = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_was_there_negative_participant = models.CharField(max_length=255, widget=widgets.RadioSelect(),choices=['Ja', 'Nein'])
    q2_negative_participant = models.TextField(default='Fügen Sie hier die Spielernamen hinzu.')
    q2_was_there_positive_participant = models.CharField(max_length=255,
                                                         widget=widgets.RadioSelect(), choices=['Ja', 'Nein'])
    q2_positive_participant = models.TextField(default='Fügen Sie hier die Spielernamen hinzu.')

    # confidant
    q2_confidant_followed_chat_intstructions = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_difficulty_chat_instructions = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_problems_chat_instructions = models.TextField()
    q2_confidant_others_found_out_confidant = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_others_found_out_confidant_why = models.TextField()
    q2_confidant_pleased_about_being_chosen = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_would_have_participated_if_knew = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_comments_in_general = models.TextField()
    q2_confidant_influence_inputs = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_inputs_being_ignored_others = models.PositiveIntegerField(min=1, max=10, widget=widgets.SliderInput(show_value=False))
    q2_confidant_cleaning_how_to_proceed = models.CharField(max_length=255, widget=widgets.RadioSelect(),choices=['Die Gruppe einigte sich auf klare Regeln, wie sich jeder im Spiel verhalten soll.',
                                                                                                                  'Es wurde vage vereinbart, wie sich jeder im Spiel verhalten soll.',
                                                                                                                  'Verschiedene Möglichkeiten, wie sich jeder im Spiel verhalten soll, wurden angesprochen, aber es kam nie zu einer Einigung auf eine der Möglichkeiten.',
                                                                                                                  'Obschon keine konkreten Möglichkeiten genannt wurden, wie sich jeder im Spiel verhalten soll wurde mir klarer, wie ich meine Entscheidungen verbessern könnte.',
                                                                                                                  'Es wurde zwar über das Reinigen bzw. Verhalten im Spiel geredet, dies hatte aber keinen Bezug darauf, wie man in weiteren Spielen handeln soll.',
                                                                                                                  'Das Thema \'Toilettenreinigung\' bzw. Verhalten im Spiel wurde gar nicht angesprochen'])

    q2_confidant_how_to_realize_recommendations = models.TextField()

