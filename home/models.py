from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from modelcluster.fields import ParentalKey

from core.models import LabPage
from articles.models import ProjectPage, PublicationPage, PersonPage

## HomePage
#
#  This models the main splash page for the website.
#
class HomePage(LabPage):
  brief_title = models.CharField(max_length=250, blank=True)
  blurb = RichTextField(blank=True)
  image = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
      null=True
      )
  secondary_image = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
      null=True, blank=True
      )

  content_panels = Page.content_panels + [
      FieldPanel('brief_title'),
      FieldPanel('blurb', classname="full"),
      ImageChooserPanel('image'),
      ImageChooserPanel('secondary_image'),
      InlinePanel('funders', label="Funders"),
      ]

  def get_context(self, request):
    # Update context to include project pages to highlight
    context = super(HomePage, self).get_context(request)
    projects = Page.objects.type(ProjectPage).live()
    people = Page.objects.type(ProjectPage).live()
    publications = Page.objects.type(PublicationPage).live()
    context['projects'] = projects
    context['people'] = people
    context['publications'] = publications
    return context


## HomePageFunder
#
#  A funder to be displayed on the home page.
#
class HomePageFunder(Orderable):
  page = ParentalKey(HomePage, related_name='funders')
  logo = models.ForeignKey(
      'wagtailimages.Image', on_delete=models.CASCADE, related_name='+',
      null=True
      )
  link = models.URLField(null=True, blank=True)

  panels = [
      ImageChooserPanel('logo'),
      FieldPanel('link'),
      ]
