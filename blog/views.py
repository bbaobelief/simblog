# -*- coding: utf-8 -*-
from base.mixins.views import SimblogListView,SimblogDetailView

from .models import *

class BlogList(SimblogListView):
    model = Article
    template_name = 'blog/blog_list.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(BlogList, self).get_context_data(**kwargs)
        context['categories'] = ['python','django','python','nosql','life','web','uuuu','234234']
        return context


class BlogDetail(SimblogDetailView):
    model = Article
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(BlogDetail, self).get_context_data(**kwargs)
        # context['breadcrumb'].extend([
        #     (u'项目总览', reverse_lazy('project_list')),
        #     (self.object.name, ''),
        # ])
        return context