# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 16:44
from __future__ import unicode_literals

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('toilet_questionnaire_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='q2_describe_actions',
            field=otree.db.models.LongStringField(null=True),
        ),
    ]