# -*- coding: utf-8 -*-
from django.contrib import admin
from models import Article, Author, Tag, Category, Link


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'is_show', 'author', 'publish_time', 'is_top')
    list_display_links = ('title', 'id')
    list_filter = ('publish_time',)
    ordering = ('-publish_time',)
    filter_horizontal = ('tag',)
    list_editable = ('is_show', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    search_fields = ('name',)
    ordering = ('order',)
    list_editable = ('name', 'order')


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'create_time')
    search_fields = ('name',)
    ordering = ('create_time',)
    list_editable = ('name',)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_show', 'website')
    search_fields = ('name',)
    ordering = ('name',)
    list_editable = ('name', 'is_show', 'website')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Link, LinkAdmin)
