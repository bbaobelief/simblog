# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(unique=True, max_length=50, verbose_name='\u6807\u9898'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(unique=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=20, verbose_name='\u5206\u7c7b', db_index=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(unique=True, max_length=30, db_index=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=20, db_index=True),
        ),
    ]
