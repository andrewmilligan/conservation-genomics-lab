# Generated by Django 2.1.4 on 2018-12-16 00:53

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtaildocs', '0008_document_file_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PersonPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('position', models.CharField(blank=True, max_length=250)),
                ('blurb', wagtail.core.fields.RichTextField(blank=True)),
                ('bio', wagtail.core.fields.RichTextField(blank=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ProjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('blurb', wagtail.core.fields.RichTextField(blank=True)),
                ('body', wagtail.core.fields.StreamField([('heading', wagtail.core.blocks.CharBlock(classname='full title', icon='title')), ('textblock', wagtail.core.blocks.RichTextBlock(label='Text Block')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(null=True, required=False)), ('subtitle', wagtail.core.blocks.CharBlock(null=True, required=False)), ('caption', wagtail.core.blocks.RichTextBlock(null=True, required=False)), ('credit', wagtail.core.blocks.CharBlock(null=True, required=False)), ('max_width', wagtail.core.blocks.IntegerBlock(help_text='maximum width of image in pixels', min_value=0, null=True, required=False))])), ('pullquote', wagtail.core.blocks.BlockQuoteBlock(label='Pull Quote'))])),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='PublicationPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('author_list', wagtail.core.fields.StreamField([('author', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('institution', wagtail.core.blocks.CharBlock(null=True, required=False))]))], blank=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('abstract', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('journal', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('pdf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
