# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dirbrowse', '0013_auto_20160624_1847'),
    ]

    operations = [
        migrations.AddField(
            model_name='dirbrowsepage',
            name='news_feed_url',
            field=models.URLField(blank=True, help_text='Link to a WordPress Feed from the Library News Site'),
        ),
    ]
