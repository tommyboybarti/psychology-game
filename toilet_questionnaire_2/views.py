# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class PlaceboQ2(Page):

    form_model = models.Player
    form_fields = [

        'q2_communication_surprised', 'q2_communication_satisfied', 'q2_communication_upset',
        'q2_fair_discussion',
        'q2_fear_criticism',
        'q2_communication_to_be_right',
        'q2_give_opinion',
        'q2_others_opinions',
        'q2_communication_whine',
        'q2_inputs_considered',
        'q2_best_player',
        'q2_communication_focused',
        'q2_communication_efficient',
        'q2_communication_interested_in_solution',
        'q2_discussion_tense',
        'q2_discussion_tense_why',
        'q2_chat_instructions_helpful',
        'q2_chat_instructions_followed',
        'q2_was_there_negative_participant',
        'q2_negative_participant',
        'q2_was_there_positive_participant',
        'q2_positive_participant',
        'q2_describe_actions'
    ]

    def q2_best_player_choices(self):

        choices = []
        for player in self.group.get_players():

            if player.id_in_group == self.player.id_in_group:
                choices.append('Ich')
            else:
                choices.append('Spieler ' + str(player.id_in_group))

        choices.append('Niemand (alle trugen gleich viel bei)')

        return choices

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get('is_negative_confidant', False):
            return False

        return True


class ConfidantQ2(Page):

    form_model = models.Player
    form_fields = [

        'q2_confidant_followed_chat_intstructions',
        'q2_confidant_difficulty_chat_instructions',
        'q2_confidant_problems_chat_instructions',
        'q2_confidant_others_found_out_confidant',
        'q2_confidant_others_found_out_confidant_why',
        'q2_confidant_pleased_about_being_chosen',
        'q2_confidant_would_have_participated_if_knew',
        'q2_confidant_comments_in_general',
        'q2_confidant_influence_inputs',
        'q2_confidant_inputs_being_ignored_others',
        'q2_confidant_cleaning_how_to_proceed',
        'q2_confidant_how_to_realize_recommendations'
    ]

    def is_displayed(self):
        if self.player.participant.vars.get('is_positive_confidant', False) or self.player.participant.vars.get('is_negative_confidant', False):
            return True

        return False


page_sequence = [
    ConfidantQ2, PlaceboQ2
]
