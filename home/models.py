from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel

from core.models import LabPage, HighlightPage

class HomePage(LabPage):
  brief_title = models.CharField(max_length=250, blank=True)
  blurb = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
      null=True
      )

  content_panels = Page.content_panels + [
      FieldPanel('brief_title'),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      ]

  def get_context(self, request):
    # Update context to include project pages to highlight
    context = super(HomePage, self).get_context(request)
    projects = Page.objects.type(HighlightPage).live()
    context['projects'] = projects
    return context

