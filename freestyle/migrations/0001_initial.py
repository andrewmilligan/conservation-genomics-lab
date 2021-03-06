# Generated by Django 2.1.4 on 2019-03-30 20:57

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreestylePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('carousel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200)), ('images', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('blurb', wagtail.core.blocks.RichTextBlock(required=False)), ('page', wagtail.core.blocks.PageChooserBlock(required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Ignored if page is set', required=False))])))])), ('image_link_columns', wagtail.core.blocks.StructBlock([('image_links', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock(required=False))]))), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')]))])), ('text_columns', wagtail.core.blocks.StructBlock([('columns', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('text', wagtail.core.blocks.RichTextBlock(required=False))]))), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')]))])), ('recent_publications', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')]))])), ('current_projects', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(max_length=200, required=False)), ('style', wagtail.core.blocks.ChoiceBlock(choices=[('dark', 'Dark'), ('light', 'Light')]))]))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
