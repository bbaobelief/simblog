# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import OldBlogList, OldBlogDetail, OldBlogSearch, OldBlogCategory
from .views import OldBlogArchive, OldBlogYearArchive, OldBlogMonthArchive

urlpatterns = [
    # Blog
    url(r'^$', OldBlogList.as_view(), name='oldblog_list'),
    url(r'^article/(?P<pk>\d+).html$', OldBlogDetail.as_view(), name='oldblog_detail'),
    url(r'^archive/$', OldBlogArchive.as_view(), name='oldblog_archive'),
    url(r'^archive/(?P<year>\d{4})/$', OldBlogYearArchive.as_view(), name='oldblog_archive_year'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d+)/$', OldBlogMonthArchive.as_view(), name='oldblog_archive_month'),
    url(r'^category/(?P<pk>\d+)/$', OldBlogCategory.as_view(), name='oldblog_category'),

    # Search
    url('^search/$', OldBlogSearch.as_view(), name='oldblog_search'),
]
