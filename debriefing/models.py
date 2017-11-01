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
    name_in_url = 'debriefing_questionnaire'
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

    # confidant
    confidant_debriefing_feedback = models.TextField()
