# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20151202_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockdata',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stockdata',
            name='time',
        ),
        migrations.AddField(
            model_name='stockdata',
            name='datetime',
            field=models.DateTimeField(default=None),
            preserve_default=False,
        ),
    ]
