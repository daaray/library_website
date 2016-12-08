# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('redirects', '0020_auto_20161103_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redirectpage',
            name='content_specialist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_content_specialist', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='redirectpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='redirectpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='redirects_redirectpage_maintainer', to='staff.StaffPage'),
        ),
    ]