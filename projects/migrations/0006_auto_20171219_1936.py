# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 19:36
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20171219_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([('heading', wagtail.wagtailcore.blocks.CharBlock(classname='full title', icon='title')), ('textblock', wagtail.wagtailcore.blocks.RichTextBlock(label='Text Block')), ('image', wagtail.wagtailcore.blocks.StructBlock([(b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'title', wagtail.wagtailcore.blocks.CharBlock(null=True, required=False)), (b'subtitle', wagtail.wagtailcore.blocks.CharBlock(null=True, required=False)), (b'caption', wagtail.wagtailcore.blocks.RichTextBlock(null=True, required=False)), (b'credit', wagtail.wagtailcore.blocks.CharBlock(null=True, required=False))])), ('pullquote', wagtail.wagtailcore.blocks.BlockQuoteBlock(label='Pull Quote'))]),
        ),
    ]