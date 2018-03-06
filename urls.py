# urls.py
from django.conf.urls import url, include
from otree.urls import urlpatterns

urlpatterns.append(
    url(r'^ajax_chat/', include('chat.ajax', namespace="ajax_chat"))
)
