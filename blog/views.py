# -*- coding: utf-8 -*-
from base.mixins.views import SimblogListView

from .models import *

def Get_Category(lis):
    cate_list = []
    for c in lis:
        if lis.index(c) >= len(lis)/2:
          print c,"++++"
          return cate_list.append(c)
        else:
          print c,"----"
          return cate_list.append(c)

lis = ['python','django','python','nosql','life','web']

class ProjectList(SimblogListView):
    model = User
    template_name = 'blog/page-blog.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super(ProjectList, self).get_context_data(**kwargs)
        context['categories'] = lis
        return context