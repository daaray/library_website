# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-20 18:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0013_make_rendition_upload_callable'),
        ('conferences', '0050_auto_20160913_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferenceindexpage',
            name='banner_feature',
            field=models.ForeignKey(blank=True, help_text='Banner feature images should be approximately 500 × 500 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='conferencepage',
            name='banner_feature',
            field=models.ForeignKey(blank=True, help_text='Banner feature images should be approximately 500 × 500 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='conferencesubpage',
            name='banner_feature',
            field=models.ForeignKey(blank=True, help_text='Banner feature images should be approximately 500 × 500 pixels', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
