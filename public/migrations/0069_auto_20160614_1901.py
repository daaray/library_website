# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0068_auto_20160610_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='standardpage',
            name='display_hierarchical_listing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='enable_index',
            field=models.BooleanField(default=False),
        ),
    ]
