# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-27 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lib_collections', '0050_exhibitpage_web_exhibit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exhibitpage',
            name='web_exhibit',
            field=models.BooleanField(default=False, help_text='Display as web exhibit'),
        ),
    ]
