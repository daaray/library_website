# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-23 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0011_auto_20160623_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirbrowsepage',
            name='events_feed_url',
            field=models.URLField(blank=True),
        ),
    ]
