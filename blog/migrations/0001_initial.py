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
                ('is_top', models.BooleanField(default=False, verbose_name='\u7f6e\u9876')),
                ('counts', models.IntegerField(default=0, verbose_name='\u70b9\u51fb\u7387', blank=True)),
                ('is_show', models.CharField(default=b'True', max_length=100, verbose_name='\u52a0\u5bc6', choices=[(b'True', '\u663e\u793a'), (b'False', '\u9690\u85cf')])),
                ('source', models.CharField(default=b'yuanchuang', max_length=30, verbose_name='\u6765\u6e90', choices=[(b'yuanchuang', '\u539f\u521b'), (b'zhuanzai', '\u8f6c\u8f7d')])),
                ('source_link', models.URLField(blank=True)),
                ('publish_time', models.DateTimeField(auto_now_add=True, verbose_name='\u53d1\u5e03\u65f6\u95f4')),
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
                ('avatar', models.ImageField(default=b'avatar/default.png', upload_to=b'avatar/%Y/%m', verbose_name='\u5934\u50cf', blank=True)),
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
                ('name', models.CharField(max_length=20, verbose_name='\u5206\u7c7b', db_index=True)),
                ('sorting', models.IntegerField(default=10, verbose_name='\u6392\u5e8f', blank=True)),
            ],
            options={
                'ordering': ['sorting', 'id'],
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, db_index=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('website', models.URLField()),
                ('sorting', models.IntegerField(default=0, verbose_name='\u6392\u5e8f', blank=True)),
            ],
            options={
                'ordering': ['sorting', 'id'],
                'verbose_name': '\u53cb\u94fe',
                'verbose_name_plural': '\u53cb\u94fe',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, db_index=True)),
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
            field=models.ForeignKey(default=1, verbose_name='\u4f5c\u8005', to='blog.Author'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(default=1, verbose_name='\u5206\u7c7b', to='blog.Category'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='\u6807\u7b7e', blank=True),
        ),
    ]
