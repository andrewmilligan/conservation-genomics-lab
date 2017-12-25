# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 22:04
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_personpage_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personpage',
            old_name='headshot',
            new_name='image',
        ),
        migrations.AddField(
            model_name='personpage',
            name='blurb',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True),
        ),
    ]