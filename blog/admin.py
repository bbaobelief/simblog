# -*- coding: utf-8 -*-
from django.contrib import admin
from models import *

class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    """docstring for ArticleAdmin"""
    list_display = ('id','title','category','counts','is_show','author','publish_time','is_top') #指定要显示的字段
    list_display_links = ('title', 'id', ) #指定可以点击的字段
    list_filter = ('publish_time',)        #指定列表过滤器，右边将会出现一个快捷的日期过滤选项，
    date_hierarchy = 'publish_time'        #日期型字段进行层次划分
    ordering = ('-publish_time',)          #对日期降序排列
    filter_horizontal = ('tags',)          #水平过滤器
    list_editable = ('counts','is_show','category')  #列表页可编辑

    # 分组表单
    # fieldsets = (
    #     (u'基本信息', {
    #         'fields': ('title', 'author', 'content', 'category', )
    #     }),
    #     (u'高级设置', {
    #         'classes': ('collapse',),
    #         'fields': ('is_top', 'counts',)
    #     }),
    # )

    class Media:
        css = {  
              'all': ('/static/kindeditor/plugins/code/prettify.css',),
        } 
        js = (
            '/static/kindeditor/kindeditor-min.js',
            '/static/kindeditor/lang/zh_CN.js',
            '/static/kindeditor/config.js',
            '/static/kindeditor/plugins/code/code.js',
        )

class CategoryAdmin(admin.ModelAdmin):
    """docstring for CategoryAdmin"""
    list_display = ('id', 'name', 'sorting')
    search_fields = ('name',)
    ordering = ('sorting',)          #对日期降序排列
    list_editable = ('name', 'sorting')  #列表页可编辑

class TagAdmin(admin.ModelAdmin):
    """docstring for TagAdmin"""
    list_display = ('id', 'tag_name', 'create_time')
    search_fields = ('tag_name',)
    ordering = ('create_time',)          #对日期降序排列
    list_editable = ('tag_name', )  #列表页可编辑

class LinkAdmin(admin.ModelAdmin):
    """docstring for LinkAdmin"""
    list_display = ('id', 'name', 'email', 'website')
    search_fields = ('name',)
    ordering = ('name',)          #对日期降序排列
    list_editable = ('name', 'email', 'website', )  #列表页可编辑

admin.site.register(Author,AuthorAdmin)
admin.site.register(Article)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Link,LinkAdmin)