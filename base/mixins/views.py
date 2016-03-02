# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.views.generic.base import ContextMixin
from blog.models import Category, Article, Tag


# from django.contrib.messages.views import SuccessMessageMixin
# from django.contrib import messages

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class SidebarMixin(ContextMixin):
    """
    Public Sidebar
    """
    def get_context_data(self, **kwargs):
        context = super(SidebarMixin, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['articles'] = Article.objects.filter(is_show='True').order_by("-publish_time")[0:10]
        context['tags'] = Tag.objects.all()
        return context

class SimListView(ListView, SidebarMixin):
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(SimListView, self).get_context_data(**kwargs)
        return context


class SimDetailView(DetailView, SidebarMixin):
    def get_context_data(self, **kwargs):
        context = super(SimDetailView, self).get_context_data(**kwargs)
        return context


# class BeaconCreateView(LoginRequiredMixin, BreadcrumbMixin, SuccessMessageMixin, CreateView):
#     template_name = 'layout/add.html'
#     success_message = u'%s创建成功'

#     def get_context_data(self, **kwargs):
#         context = super(BeaconCreateView, self).get_context_data(**kwargs)
#         context['page_name'] = (self.model._meta.verbose_name, '新增')
#         return context

#     def get_success_message(self, cleaned_data):
#         self.success_message = self.success_message % self.object
#         return super(BeaconCreateView, self).get_success_message(cleaned_data)


# class BeaconUpdateView(LoginRequiredMixin, BreadcrumbMixin, SuccessMessageMixin, UpdateView):
#     template_name = 'layout/update.html'
#     success_message = u'%s更新成功'

#     def get_context_data(self, **kwargs):
#         context = super(BeaconUpdateView, self).get_context_data(**kwargs)
#         context['page_name'] = (self.model._meta.verbose_name, self.object)
#         return context

#     def get_success_message(self, cleaned_data):
#         self.success_message = self.success_message % self.object
#         return super(BeaconUpdateView, self).get_success_message(cleaned_data)


# class BeaconDeleteView(LoginRequiredMixin, BreadcrumbMixin, SuccessMessageMixin, DeleteView):
#     template_name = 'layout/delete.html'
#     success_message = u'%s删除成功'

#     def get_context_data(self, **kwargs):
#         context = super(BeaconDeleteView, self).get_context_data(**kwargs)
#         context['page_name'] = (self.model._meta.verbose_name, self.object)
#         return context

#     def delete(self, request, *args, **kwargs):
#         messages.success(request, self.success_message % self.get_object())
#         return super(BeaconDeleteView, self).delete(request, *args, **kwargs)