# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-01 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0042_auto_20160205_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationpage',
            name='email_label',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='locationpage',
            name='phone_label',
            field=models.CharField(blank=True, max_length=254),
        ),
    ]
