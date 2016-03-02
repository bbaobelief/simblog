# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import BlogListView, BlogDetailView, BlogSearchView, BlogCategoryView
from .views import BlogArchiveView, BlogYearArchiveView, BlogMonthArchiveView
from .models import Article

urlpatterns = [
    # Blog
    url(r'^$', BlogListView.as_view(), name='blog_list'),
    url(r'^article/(?P<pk>\d+).html$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^archive/$', BlogArchiveView.as_view(), name='blog_archive'),
    url(r'^archive/(?P<year>\d{4})/$', BlogYearArchiveView.as_view(), name='blog_archive_year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', BlogMonthArchiveView.as_view(), name='blog_archive_month'),
    url(r'^category/(?P<pk>\d+)/$', BlogCategoryView.as_view(), name='blog_category'),

    # Search
    url('^search/$', BlogSearchView.as_view(), name='blog_search'),
]