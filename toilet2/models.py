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
    num_rounds = 3
    available_group_sizes = (3, 4, 5)

    max_toilet = 10.
    max_health = 10


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

    toilet = models.FloatField(min=0, max=Constants.max_toilet, default=3)

    def init_group(self):
        if self.round_number == 1:
            self.toilet = 3
        else:
            prev_round = self.in_round(self.round_number - 1)
            self.toilet = prev_round.toilet

        for player in self.get_players():
            if self.round_number == 1:
                player.health = 10
                player.resources = 10
            else:
                player_prev_round = player.in_round(self.round_number - 1)
                player.resources = (
                    player_prev_round.resources + 3)
                player.health = player_prev_round.health + 1
                if player.health > Constants.max_health:
                    player.health = Constants.max_health

    def set_payoff(self):
        players = self.get_players()
        toilet_dirt, part_of_big_clean = 0., []
        dont_use_the_toilet = sum(1 for player in players if not player.use_toilet)
        toilet_usage_health_lose = 2

        for player in players:
            if not player.health:
                continue # if player is dead don't play

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
            if player.health > Constants.max_health:
                player.health = Constants.max_health

            if player.big_clean:
                part_of_big_clean.append(player)


        # set the new status of toilet
        self.toilet -= toilet_dirt
        if self.toilet < 0:
            self.toilet = 0

        # big clean
        if part_of_big_clean:
            contribution, resources = int(20/len(part_of_big_clean)), 0.
            for player in part_of_big_clean:
                if player.resources >= contribution:
                    resources += contribution
                    player.resources -= contribution
                else:
                    resources += player.resources
                    player.resources = 0
            clean_prop =  resources / 20.
            self.toilet += (20. - self.toilet) * clean_prop
        if self.toilet < 0:
            self.toilet = 0
        elif self.toilet > 20:
            self.toilet = 20

        # in the last round set the resources as payoff
        if self.round_number == Constants.num_rounds:
            for player in players:
                player.payoff = player.resources


class Player(BasePlayer):

    health = models.PositiveIntegerField(min=0, max=Constants.max_health)
    resources = models.PositiveIntegerField(min=0)

    use_toilet = models.BooleanField(widget=widgets.RadioSelectHorizontal())
    small_cleaning = models.BooleanField(widget=widgets.RadioSelectHorizontal())

    big_clean = models.BooleanField(widget=widgets.RadioSelectHorizontal())

