# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-11-04 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0052_auto_20161103_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unitindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units_unitindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='unitindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units_unitindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='unitpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units_unitpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='unitpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units_unitpage_maintainer', to='staff.StaffPage'),
        ),
    ]
