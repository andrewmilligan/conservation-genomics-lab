# Generated by Django 2.1.4 on 2019-01-24 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectpage',
            name='promoted',
            field=models.BooleanField(default=False, help_text='Promoted pages are highlighted on the home page'),
        ),
    ]
