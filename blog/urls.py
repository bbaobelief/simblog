# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import ProjectList

urlpatterns = [
    # Blog
    url(r'^$', ProjectList.as_view(), name='project_list'),
    url(r'^blog/$', ProjectList.as_view(), name='project_list'),
    # url(r'^project/add/$', ProjectCreate.as_view(), name='project_create'),
    # url(r'project/(?P<pk>\d+)/$', ProjectDetail.as_view(), name='project_detail'),
    # url(r'^project/(?P<pk>\d+)/update/$', ProjectUpdate.as_view(), name='project_update'),
    # url(r'^project/(?P<pk>\d+)/delete/$', ProjectDelete.as_view(), name='project_delete'),

]