# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """标签"""
    name = models.CharField(u'名称', max_length=20, unique=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Category(models.Model):
    """分类"""
    name = models.CharField(u'分类', max_length=20, unique=True)
    order = models.IntegerField(u'顺序', default=10, blank=True)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name
        ordering = ['order', 'id']

    def __unicode__(self):
        return self.name


class Author(models.Model):
    """作者"""
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    avatar = models.ImageField(upload_to='uploads/avatar/%Y/%m', blank=True, default='uploads/avatar/default.png')

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.name)


class Article(models.Model):
    """文章"""
    SOURCE_CHOICE = (
                        ('original', u'原创'),
                        ('reprint', u'转载')
                    )

    title = models.CharField(u'标题', max_length=50)
    content = models.TextField(u'内容')
    counts = models.IntegerField(u'点击率', default=0, blank=True)
    is_top = models.BooleanField(u'置顶', default=False)
    is_show = models.BooleanField(u'加密', default=False)
    author = models.ForeignKey(Author, default=1, related_name='author_article', verbose_name=u'作者')
    category = models.ForeignKey(Category, default=1, related_name='category_article', verbose_name=u'分类')
    tag = models.ManyToManyField(Tag, blank=True, related_name='tag_article', verbose_name=u'标签')
    source = models.CharField(u'来源', max_length=30, choices=SOURCE_CHOICE, default='original')
    source_link = models.URLField(blank=True)
    publish_time = models.DateTimeField(u'发布时间', auto_now_add=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True)

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_time']

    def __unicode__(self):
        return self.title


class Link(models.Model):
    """友链"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField()
    is_show = models.BooleanField(u'显示', default=True)
    order = models.IntegerField(u'顺序', default=0, blank=True)

    class Meta:
        verbose_name = u'友链'
        verbose_name_plural = verbose_name
        ordering = ['order', 'id']

    def __unicode__(self):
        return self.name
