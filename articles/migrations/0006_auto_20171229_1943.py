# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-29 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20171229_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicationpage',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
