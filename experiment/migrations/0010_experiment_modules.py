# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 14:36
from __future__ import unicode_literals

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('experiment', '0009_experiment_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiment',
            name='modules',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='experiment.Module'),
        ),
    ]