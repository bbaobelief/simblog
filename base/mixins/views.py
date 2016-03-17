# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.base import ContextMixin
from django.db.models import Count
from blog.models import Category, Article, Tag, Link


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class SidebarMixin(ContextMixin):
    """Public Sidebar"""
    def get_context_data(self, **kwargs):
        context = super(SidebarMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(is_show='True').order_by("-publish_time")[0:10]
        tag_count = Article.objects.values('tag').exclude(tag=None).annotate(count=Count('tag')).order_by('-count')
        context['tags'] = [[Tag.objects.get(pk=t['tag']),t['count']] for t in tag_count]
        context['links'] = Link.objects.all()
        return context


class SimListView(ListView, SidebarMixin):
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(SimListView, self).get_context_data(**kwargs)
        return context


class SimDetailView(DetailView, SidebarMixin):
    def get_context_data(self, **kwargs):
        context = super(SimDetailView, self).get_context_data(**kwargs)
        return context
