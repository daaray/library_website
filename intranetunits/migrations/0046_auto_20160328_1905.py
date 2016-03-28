# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-28 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intranetunits', '0045_auto_20160307_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intranetunitsindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitsindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitspage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitspage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitspage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitspage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitsreportsindexpage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsreportsindexpage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitsreportsindexpage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsreportsindexpage_maintainer', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitsreportspage',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsreportspage_editor', to='staff.StaffPage'),
        ),
        migrations.AlterField(
            model_name='intranetunitsreportspage',
            name='page_maintainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='intranetunits_intranetunitsreportspage_maintainer', to='staff.StaffPage'),
        ),
    ]
