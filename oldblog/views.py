# -*- coding: utf-8 -*-
from blog.views import BlogList, BlogDetail, BlogSearch, BlogCategory
from blog.views import BlogArchive, BlogYearArchive, BlogMonthArchive


class OldBlogList(BlogList):
    paginate_by = 5
    template_name = 'oldblog/blog_list.html'
    context_object_name = 'article'


class OldBlogDetail(BlogDetail):
    template_name = 'oldblog/blog_detail.html'


class OldBlogSearch(BlogSearch):
    template_name = 'oldblog/blog_list.html'
    context_object_name = 'article'


class OldBlogArchive(BlogArchive):
    template_name = 'oldblog/archive/archive_list.html'


class OldBlogYearArchive(BlogYearArchive):
    template_name = 'oldblog/archive/archive_year.html'


class OldBlogMonthArchive(BlogMonthArchive):
    template_name = 'oldblog/archive/archive_month.html'


class OldBlogCategory(BlogCategory):
    template_name = 'oldblog/blog_list.html'
