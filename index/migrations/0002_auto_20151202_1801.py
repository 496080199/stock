# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockData',
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
        migrations.RenameField(
            model_name='stock',
            old_name='name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='high',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='low',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='now',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='now_minus',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='now_plus',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='start',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='time',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='yesterday',
        ),
        migrations.AddField(
            model_name='stock',
            name='code',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stockdata',
            name='stock',
            field=models.ForeignKey(to='index.Stock'),
        ),
    ]
