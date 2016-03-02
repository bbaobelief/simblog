# -*- coding: utf-8 -*-
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from base.mixins.views import SimListView, SimDetailView, SidebarMixin
from .models import Article

class BlogListView(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        return context


class BlogDetailView(SimDetailView):
    model = Article
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        return context


class BlogSearchView(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        search = self.request.POST.get('title', None)
        queryset = super(BlogSearchView, self).get_queryset()
        queryset = queryset.filter(title__icontains = search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogSearchView, self).get_context_data(**kwargs)
        context['search'] = self.request.POST.get('title', None)
        return context


class BlogArchiveView(ArchiveIndexView, SidebarMixin):
    """归档"""
    model=Article
    queryset = Article.objects.all()
    paginate_by = 20
    date_field = "publish_time"
    context_object_name = 'archive_list'
    template_name = 'blog/archive_list.html'


class BlogYearArchiveView(YearArchiveView, SidebarMixin):
    """按年归档"""
    queryset = Article.objects.filter(is_show='True').order_by("-publish_time")
    date_field = "publish_time"
    make_object_list = True
    allow_future = True
    context_object_name = 'archive_list'
    template_name = 'blog/archive_year.html'


class BlogMonthArchiveView(MonthArchiveView, SidebarMixin):
    """按月归档"""
    queryset = Article.objects.filter(is_show='True').order_by("-publish_time")
    date_field = "publish_time"
    allow_future = True
    month_format = '%m'
    context_object_name = 'archive_list'
    template_name = 'blog/archive_month.html'


class BlogCategoryView(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_queryset(self):
        self.pk = self.kwargs['pk']
        return Article.objects.filter(category=self.pk)

    def get_context_data(self, **kwargs):
        context = super(BlogCategoryView, self).get_context_data(**kwargs)
        return context
