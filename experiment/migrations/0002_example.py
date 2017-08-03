# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-03 17:23
from __future__ import unicode_literals

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name of Example')),
                ('num_trial', models.IntegerField(verbose_name='Trial Number')),
                ('alert_color', colorfield.fields.ColorField(default='#f44141', max_length=18, verbose_name='Color of Alert (green default is #4ef442)')),
                ('points', models.FloatField(verbose_name='Points from Last Trial')),
                ('score', models.FloatField(verbose_name='Score')),
                ('outcome', models.CharField(max_length=200, verbose_name='Outcome from Last Trial')),
                ('stimulus', models.CharField(choices=[('num', 'Numbers'), ('rect', 'Rectangles')], default='num', max_length=200, verbose_name='Choice of Stimulus')),
                ('val', models.FloatField(verbose_name='Value of Stimulus (rectangle value is percent of box height)')),
            ],
        ),
    ]
