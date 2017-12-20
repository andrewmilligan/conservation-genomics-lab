from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index
from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock

from utils.models import LabPage, HighlightPage


class CaptionedImageBlock(blocks.StructBlock):
  image = ImageChooserBlock()
  title = blocks.CharBlock(null=True, required=False)
  subtitle = blocks.CharBlock(null=True, required=False)
  caption = blocks.RichTextBlock(null=True, required=False)
  credit = blocks.CharBlock(null=True, required=False)

  class Meta:
    template = 'projects/blocks/captioned_image_block.html'
    icon = 'image'


class ProjectIndexPage(LabPage):
  intro = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('intro', classname="full")
      ]


class ProjectPage(HighlightPage):
  name = models.CharField(max_length=250)
  blurb = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
      null=True
      )

  body = StreamField([
      ('heading', blocks.CharBlock(classname="full title", icon='title')),
      ('textblock', blocks.RichTextBlock(label="Text Block")),
      ('image', CaptionedImageBlock()),
      ('pullquote', blocks.BlockQuoteBlock(label="Pull Quote")), 
      ])

  search_fields = Page.search_fields + [
      index.SearchField('name'),
      index.SearchField('blurb'),
      index.SearchField('body'),
      ]

  content_panels = Page.content_panels + [
      FieldPanel('name'),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      StreamFieldPanel('body'),
      ]

