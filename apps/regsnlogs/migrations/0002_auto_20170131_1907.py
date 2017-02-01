# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 03:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regsnlogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='end_date',
            new_name='departing',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='plan',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='location',
            new_name='destination',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='start_date',
            new_name='returning',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='created_by',
            new_name='user',
        ),
    ]
