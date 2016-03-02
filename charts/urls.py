# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ChartsView

urlpatterns = [
    # Charts
    url(r'^$', ChartsView.as_view(), name='charts_view'),
]