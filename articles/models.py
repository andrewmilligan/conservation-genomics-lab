from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from core.models import LabPage, HighlightPage
from blocks import CaptionedImageBlock


class ArticleIndexPage(LabPage):
  intro = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('intro', classname="full")
      ]

  subpage_types = ['articles.PersonPage', 'articles.ProjectPage']


class PersonPage(LabPage):
  email = models.EmailField(blank=True)
  position = models.CharField(max_length=250, blank=True)
  blurb = RichTextField(blank=True)
  bio = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image',
      on_delete=models.SET_NULL,
      related_name='+',
      null=True
      )

  search_fields = Page.search_fields + [
      index.SearchField('position'),
      index.SearchField('bio'),
      index.SearchField('blurb'),
      ]

  content_panels = Page.content_panels + [
      FieldPanel('email'),
      FieldPanel('position'),
      FieldPanel('bio', classname="full"),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      ]

  parent_page_types = ['articles.ArticleIndexPage']


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
