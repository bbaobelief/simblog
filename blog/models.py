# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    """标签"""
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = u'标签'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.tag_name


class Category(models.Model):
    name = models.CharField(u'分类', max_length=20)
    sorting = models.IntegerField(u'排序', default=10, blank=True)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = verbose_name
        ordering = ['sorting', 'id']

    def __unicode__(self):
        return self.name


class Author(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    avatar = models.ImageField(u'头像', upload_to='uploads/avatar/%Y/%m', blank=True, default='uploads/avatar/default.png')

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.name)


class Article(models.Model):
    title = models.CharField(u'标题', max_length=50)
    content = models.TextField(u'内容')
    author = models.ForeignKey(Author, default=1, verbose_name=u'作者')
    category = models.ForeignKey(Category, default=1, verbose_name=u'分类')
    tags = models.ManyToManyField(Tag, blank=True, verbose_name=u'标签')
    is_top = models.BooleanField(u'置顶', default=False)
    counts = models.IntegerField(u'点击率', default=0, blank=True)
    show_type = (('True', u'显示'), ('False', u'隐藏'))
    is_show = models.CharField(u'加密', max_length=100, choices=show_type, default='True')
    source_type = (('yuanchuang', u'原创'), ('zhuanzai', u'转载'))
    source = models.CharField(u'来源', max_length=30, choices=source_type, default='yuanchuang')
    source_link = models.URLField(blank=True)
    publish_time = models.DateTimeField(u'发布时间', auto_now_add=True)

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
    sorting = models.IntegerField(u'排序', default=0, blank=True)

    class Meta:
        verbose_name = u'友链'
        verbose_name_plural = verbose_name
        ordering = ['sorting', 'id']

    def __unicode__(self):
        return self.name
