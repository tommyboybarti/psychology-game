#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from chat import views

urlpatterns = [
    url(r'^send_message/$', views.send_message, name='send_message'),
    url(r'^retrieve_messages/$', views.retrieve_messages, name='retrieve_messages'),
    url(r'^export/$', views.export, name='export'),
]
