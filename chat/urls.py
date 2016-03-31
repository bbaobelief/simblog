# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ChatView

urlpatterns = [
    # Chat
    url(r'^$', ChatView.as_view(), name='chat_view'),
]