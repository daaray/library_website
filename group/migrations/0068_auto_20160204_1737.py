# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 17:37
from __future__ import unicode_literals

import base.models
from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0067_auto_20160203_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouppage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Subtle')])), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StreamBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False))), label='event'), help_text='A talk or event with a title, presenter             room number, and description', icon='edit'))), icon='date', template='base/blocks/agenda.html')))),
        ),
        migrations.AlterField(
            model_name='grouppage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h2.html')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h3.html')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h4.html')), ('h5', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h5.html')), ('h6', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title', template='base/blocks/h6.html')), ('paragraph', wagtail.wagtailcore.blocks.StructBlock((('paragraph', wagtail.wagtailcore.blocks.RichTextBlock()),))), ('image', wagtail.wagtailcore.blocks.StructBlock((('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('title', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('citation', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('caption', wagtail.wagtailcore.blocks.TextBlock(required=False)), ('alt_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('alignment', base.models.ImageFormatChoiceBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('lightbox', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False))), label='Image')), ('blockquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock(required=False))))), ('button', wagtail.wagtailcore.blocks.StructBlock((('button_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-default', 'Subtle')])), ('button_text', wagtail.wagtailcore.blocks.CharBlock(max_length=20)), ('link_external', wagtail.wagtailcore.blocks.URLBlock(required=False)), ('link_page', wagtail.wagtailcore.blocks.PageChooserBlock(required=False)), ('link_document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(required=False))))), ('video', wagtail.wagtailembeds.blocks.EmbedBlock(icon='media')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('ocaml', 'OCaml'), ('php5', 'PHP'), ('html+php', 'PHP/HTML'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')])), ('code', wagtail.wagtailcore.blocks.TextBlock())))), ('agenda_item', wagtail.wagtailcore.blocks.StreamBlock((('start_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), ('end_time', wagtail.wagtailcore.blocks.TimeBlock(required=False)), ('session_title', wagtail.wagtailcore.blocks.CharBlock(help_text='Title of the session.             Can be used as title of the talk in some situations.', required=False)), ('event', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(help_text='Talk title, workshop title, etc.', required=False)), ('presenters', wagtail.wagtailcore.blocks.CharBlock(help_text='Comma separated list of presenters             (if more than one)', required=False)), ('room_number', wagtail.wagtailcore.blocks.CharBlock(required=False)), ('description', wagtail.wagtailcore.blocks.RichTextBlock(required=False))), label='event'), help_text='A talk or event with a title, presenter             room number, and description', icon='edit'))), icon='date', template='base/blocks/agenda.html'))), blank=True),
        ),
    ]
