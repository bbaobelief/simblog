# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='is_show',
            field=models.BooleanField(default=True, verbose_name='\u663e\u793a'),
        ),
    ]
