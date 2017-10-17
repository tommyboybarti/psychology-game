# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division

import itertools
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

"""


class Constants(BaseConstants):
    name_in_url = 'chat'
    players_per_group = None
    num_rounds = 1

    available_group_sizes = (3, 4, 5)
    # treatment_small_talk = "small_talk"
    # treatment_normal_talk = "normal_talk"
    # treatments = (treatment_small_talk, treatment_normal_talk)

    treatment_placebo = "placebo_group"
    treatment_positive = "positive_group"
    treatment_positive_confidant = "confidant_positive"
    treatment_negative_confidant = "confidant_negative"

    treatments = (treatment_placebo, treatment_positive, treatment_positive_confidant, treatment_negative_confidant)



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

        # set treatments and confidants
        treatments = itertools.cycle(Constants.treatments)
        for group in self.get_groups():
            group.treatment = next(treatments)
            if group.treatment == Constants.treatment_positive_confidant:
                group.get_player_by_id(3).participant.vars['is_positive_confidant'] = 'john'









class Group(BaseGroup):

    treatment = models.CharField(choices=Constants.treatments)


class Player(BasePlayer):
    pass


# =============================================================================
# CHAT
# =============================================================================

class Message(models.Model):

    group = models.ForeignKey(Group)
    player = models.ForeignKey(Player)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    COLORS = {1: "#F249F2",
              2: "#60AB4F",
              3: "#FCC767",
              4: "#FF7979",
              5: "#F249F2"}

    @property
    def color(self):
        return Message.COLORS[self.player.id_in_group]

