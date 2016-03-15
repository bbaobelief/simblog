# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='\u6807\u9898')),
                ('content', models.TextField(verbose_name='\u5185\u5bb9')),
                ('counts', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u7387', blank=True)),
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('is_show', models.BooleanField(default=False, verbose_name='\u52a0\u5bc6')),
                ('source', models.CharField(default=b'original', max_length=30, verbose_name='\u6765\u6e90', choices=[(b'original', '\u539f\u521b'), (b'reprint', '\u8f6c\u8f7d')])),
                ('source_link', models.URLField(blank=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
            options={
                'ordering': ['-publish_time'],
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('website', models.URLField(blank=True)),
                ('avatar', models.ImageField(default=b'uploads/avatar/default.png', upload_to=b'uploads/avatar/%Y/%m', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u4f5c\u8005',
                'verbose_name_plural': '\u4f5c\u8005',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u5206\u7c7b')),
                ('order', models.IntegerField(default=10, verbose_name='\u987a\u5e8f', blank=True)),
            ],
            options={
                'ordering': ['order', 'id'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('website', models.URLField()),
                ('order', models.IntegerField(default=0, verbose_name='\u987a\u5e8f', blank=True)),
            ],
            options={
                'ordering': ['order', 'id'],
                'verbose_name': '\u53cb\u94fe',
                'verbose_name_plural': '\u53cb\u94fe',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, verbose_name='\u540d\u79f0')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(related_name='author_article', default=1, verbose_name='\u4f5c\u8005', to='blog.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(related_name='category_article', default=1, verbose_name='\u5206\u7c7b', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(related_name='tag_article', verbose_name='\u6807\u7b7e', to='blog.Tag', blank=True),
        ),
    ]
