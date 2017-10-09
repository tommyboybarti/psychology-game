# -*- coding: utf-8 -*-
from __future__ import division

from otree.common import Currency as c, currency_range, safe_json

from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Questionnaire1(Page):

    form_model = models.Player
    form_fields = [
        'q1_first_game_judge_satisfied', "q1_first_game_judge_surprised", "q1_first_game_judge_upset",

        'q1_players_helping_each_other',
        'q1_team_spirit_or_cohesion',
        'q1_important_presented_image_of_and_to_yourself',
        'q1_important_maximum_and_fair_resources_to_everyone',
        'q1_important_other_members_trust_in_you',
        'q1_important_not_you_maximum_and_fair_resources_to_everyone',
        'q1_trust_do_you_have_into_other_members',
        'q1_how_much_do_you_like_the_other_team_members',
        'q1_how_good_do_you_understand_solving',
        'q1_how_good_do_the_other_group_members_understand_solving',

        'q1_how_to_improve_the_groups_behavior_to_maximize_resources',
        'q1_which_strategy_would_you_follow_and_why',
        'q1_if_communicate_what_would_you_say_and_why']



page_sequence = [
    Questionnaire1
]
