# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('start', models.FloatField()),
                ('yesterday', models.FloatField()),
                ('now', models.FloatField()),
                ('high', models.FloatField()),
                ('low', models.FloatField()),
                ('now_plus', models.FloatField()),
                ('now_minus', models.FloatField()),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]
