# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_link_is_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='\u663e\u793a'),
        ),
    ]
