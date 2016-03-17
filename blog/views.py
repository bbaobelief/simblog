# -*- coding: utf-8 -*-
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.core.exceptions import PermissionDenied
from base.mixins.views import SimListView, SimDetailView, SidebarMixin
from .models import Article


class BlogList(SimListView):
    model = Article
    paginate_by = 10
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_queryset(self):
        queryset = super(BlogList, self).get_queryset()
        queryset = queryset.filter(is_show=True)
        return queryset


class BlogDetail(SimDetailView):
    model = Article
    template_name = 'blog/blog_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.get_object().is_show:
            raise PermissionDenied
        return super(BlogDetail, self).dispatch(request, *args, **kwargs)


class BlogSearch(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get_queryset(self):
        search = self.request.POST.get('title', None)
        queryset = super(BlogSearch, self).get_queryset().filter(title__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(BlogSearch, self).get_context_data(**kwargs)
        context['search'] = self.request.POST.get('title', None)
        return context


class BlogArchive(ArchiveIndexView, SidebarMixin):
    """归档"""
    model = Article
    queryset = Article.objects.filter(is_show=True)
    # paginate_by = 20
    date_field = "publish_time"
    context_object_name = 'archive_list'
    template_name = 'blog/archive_list.html'


class BlogYearArchive(YearArchiveView, SidebarMixin):
    """按年归档"""
    queryset = Article.objects.filter(is_show=True).order_by("-publish_time")
    date_field = "publish_time"
    make_object_list = True
    allow_future = True
    context_object_name = 'archive_list'
    template_name = 'blog/archive_year.html'


class BlogMonthArchive(MonthArchiveView, SidebarMixin):
    """按月归档"""
    queryset = Article.objects.filter(is_show=True).order_by("-publish_time")
    date_field = "publish_time"
    allow_future = True
    month_format = '%m'
    context_object_name = 'archive_list'
    template_name = 'blog/archive_month.html'


class BlogCategory(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_queryset(self):
        self.pk = self.kwargs['pk']
        return Article.objects.filter(category=self.pk)


class BlogTag(SimListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_queryset(self):
        self.pk = self.kwargs['pk']
        queryset = Article.objects.filter(tag=self.pk).filter(is_show=True).order_by("-publish_time")
        return queryset
