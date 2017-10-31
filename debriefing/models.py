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


class Subsession(BaseSubsession):
    pass


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
