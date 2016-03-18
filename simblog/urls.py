# -*- coding: utf-8 -*-
from base.upload import *
from django.conf.urls import include, url
from django.contrib import admin
from base.upload import ImageUpload

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^oldblog/', include('oldblog.urls')),
    url(r'^charts/', include('charts.urls')),
    url(r'^upload/$', ImageUpload.as_view(), name='image_upload'),
]

# Other base url
urlpatterns += [
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
]
