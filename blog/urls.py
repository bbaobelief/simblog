# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import BlogList,BlogDetail

urlpatterns = [
    # Blog
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^list/$', BlogList.as_view(), name='blog_list'),
    # url(r'^project/add/$', ProjectCreate.as_view(), name='project_create'),
    url(r'^detail/(?P<pk>\d+)/$', BlogDetail.as_view(), name='blog_detail'),
    # url(r'^project/(?P<pk>\d+)/update/$', ProjectUpdate.as_view(), name='project_update'),
    # url(r'^project/(?P<pk>\d+)/delete/$', ProjectDelete.as_view(), name='project_delete'),

]