# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import BlogList, BlogDetail, BlogSearch, BlogCategory
from .views import BlogArchive, BlogYearArchive, BlogMonthArchive

urlpatterns = [
    # Blog
    url(r'^$', BlogList.as_view(), name='blog_list'),
    url(r'^article/(?P<pk>\d+).html$', BlogDetail.as_view(), name='blog_detail'),
    url(r'^archive/$', BlogArchive.as_view(), name='blog_archive'),
    url(r'^archive/(?P<year>\d{4})/$', BlogYearArchive.as_view(), name='blog_archive_year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', BlogMonthArchive.as_view(), name='blog_archive_month'),
    url(r'^category/(?P<pk>\d+)/$', BlogCategory.as_view(), name='blog_category'),

    # Search
    url('^search/$', BlogSearch.as_view(), name='blog_search'),
]
