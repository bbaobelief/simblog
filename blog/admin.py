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

    class Media:
        css = {
            'all': (
                '/static/simditor/css/simditor.css',
                '/static/simditor/css/simditor-html.css',
                '/static/simditor/css/simditor-markdown.css',
            ),
        }
        js = (
            '/static/blog/js/jquery.js',
            '/static/simditor/js/module.js',
            '/static/simditor/js/uploader.js',
            '/static/simditor/js/hotkeys.js',
            '/static/simditor/js/simditor.js',
            '/static/simditor/js/beautify-html.js',
            '/static/simditor/js/simditor-html.js',
            '/static/simditor/js/marked.js',
            '/static/simditor/js/to-markdown.js',
            '/static/simditor/js/simditor-markdown.js',
            '/static/simditor/config.js',
        )


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
    list_display = ('id', 'name', 'email', 'website')
    search_fields = ('name',)
    ordering = ('name',)
    list_editable = ('name', 'email', 'website')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Link, LinkAdmin)
