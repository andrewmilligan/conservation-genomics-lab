from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsearch import index

from core.models import LabPage


class PeopleIndexPage(LabPage):
  intro = RichTextField(blank=True)

  content_panels = Page.content_panels + [
      FieldPanel('intro', classname="full")
      ]


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


#class PeoplePageGalleryImage(Orderable):
#  page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
#  image = models.ForeignKey(
#      'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
#      )
#  caption = models.CharField(blank=True, max_length=250)
#
#  panels = [
#      ImageChooserPanel('image'),
#      FieldPanel('caption'),
#      ]
