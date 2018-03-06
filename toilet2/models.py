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

author = 'Juan B Cabral'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'toilet2'
    players_per_group = None
    num_rounds = 2
    available_group_sizes = (3, 4, 5)

    # toilet
    start_value_toilet = 3

    max_toilet_condition = 10
    min_toilet_condition = 0



    # health
    start_value_health = 10

    min_health_condition = 0
    max_health_condition = 10

    max_health_effect = 2

    # resources
    start_value_resources = 10
    min_value_resources = 0

    resources_incrementation = 3
    max_resources_reduction = 3

    # big clean
    big_clean_cost = 20
    big_clean_min_contribution = 5


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
    toilet = models.FloatField(min=0, max=Constants.max_toilet_condition, default=Constants.start_value_toilet)

    def resources_reduction(self, player):

        return Constants.max_resources_reduction * (Constants.max_health_condition - player.health) / (
            Constants.max_health_condition - Constants.min_health_condition)

    def init_group(self):
        if self.round_number == 1:
            self.toilet = Constants.start_value_toilet
        else:
            prev_round = self.in_round(self.round_number - 1)
            self.toilet = prev_round.toilet

        for player in self.get_players():
            if self.round_number == 1:
                player.health = Constants.start_value_health
                player.resources = Constants.start_value_resources
            else:
                player_prev_round = player.in_round(self.round_number - 1)

                player.resources = (
                    player_prev_round.resources + Constants.resources_incrementation - self.resources_reduction(
                        player_prev_round))

                player.health = player_prev_round.health + 1

                if player.health > Constants.max_health_condition:
                    player.health = Constants.max_health_condition

    def current_toilet_usage_health_lose(self):

        return Constants.max_health_effect * (Constants.max_toilet_condition - self.toilet) / (
            Constants.max_toilet_condition - Constants.min_toilet_condition)

    def missing_resources(self, player, contribution):
        if player.resources < contribution:
            missing_resources = contribution - player.resources

            return missing_resources

        else:
            return 0

    def overflow_resources(self, player, contribution):
        if player.resources > contribution:
            overflow_resources = player.resources - contribution
            player.resources_overflow = overflow_resources

            return overflow_resources

        else:
            return 0

    def contribution_to_big_clean(self, player, contribution, total_resources_missing, total_resources_overflow):
        if player.resources <= contribution:
            contribution_to_big_clean = player.resources
            player.resources = 0

            return contribution_to_big_clean

        else:
            contribution_to_big_clean = contribution
            if total_resources_missing > 0:
                contribution_to_big_clean += total_resources_missing * player.resources_overflow / total_resources_overflow

            if contribution_to_big_clean < Constants.big_clean_min_contribution:
                contribution_to_big_clean = Constants.big_clean_min_contribution

            player.resources -= contribution_to_big_clean

            return contribution_to_big_clean

    def set_payoff(self):
        players = self.get_players()
        toilet_dirt, part_of_big_clean = 0., []
        dont_use_the_toilet = sum(1 for player in players if not player.use_toilet)
        toilet_usage_health_lose = self.current_toilet_usage_health_lose()

        for player in players:
            if not player.health:
                continue  # if player is dead don't play

            player.health -= dont_use_the_toilet

            if player.use_toilet:
                player.health -= toilet_usage_health_lose
                if player.small_cleaning and player.resources:
                    toilet_dirt += 0.5
                    player.resources -= 1
                else:
                    toilet_dirt += 1

            if player.health < 0:
                player.health = 0
            if player.health > Constants.max_health_condition:
                player.health = Constants.max_health_condition

            if player.big_clean:
                part_of_big_clean.append(player)

        # set the new status of toilet
        self.toilet -= toilet_dirt
        if self.toilet < 0:
            self.toilet = 0

        # big clean
        if part_of_big_clean:
            contribution, resources = int(Constants.big_clean_cost / len(part_of_big_clean)), 0.
            total_resources_missing = 0.
            total_resources_overflow = 0.

            for player in part_of_big_clean:
                total_resources_missing += self.missing_resources(player, contribution)
                total_resources_overflow += self.overflow_resources(player, contribution)
                toilet_dirt -= 0.5

            for player in part_of_big_clean:
                resources += self.contribution_to_big_clean(player, contribution, total_resources_missing,
                                                            total_resources_overflow)

            if resources >= Constants.big_clean_cost:
                self.toilet = Constants.max_toilet_condition


        # in the last round set the resources as payoff
        if self.round_number == Constants.num_rounds:
            for player in players:
                player.payoff = player.resources


class Player(BasePlayer):
    health = models.PositiveIntegerField(min=0, max=Constants.max_health_condition)
    resources = models.PositiveIntegerField(min=0)
    resources_overflow = models.PositiveIntegerField(min=0)

    use_toilet = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    small_cleaning = models.BooleanField(widget=widgets.RadioSelectHorizontal())

    big_clean = models.BooleanField(widget=widgets.RadioSelectHorizontal())
