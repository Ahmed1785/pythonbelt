# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 00:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('second_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='arrive_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='travel',
            name='travel_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]