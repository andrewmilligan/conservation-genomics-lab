from django import template

from wagtail.core.models import Page
from articles.models import ProjectPage, PublicationPage


register = template.Library()


@register.inclusion_tag("freestyle/blocks/component_title.html")
def cgri_component_title(title):
  return {
    'title': title
  }


@register.simple_tag
def cgri_column_class(n):
  if 12 % n == 0:
    return f'col-md-{int(12 / n)}'
  else:
    return 'col-md-2'


@register.inclusion_tag("freestyle/carousel.html", takes_context=True)
def cgri_carousel(context):
  '''
  This template tag is used to build the home page carousel.
  '''
  page = context['page']
  projects = ProjectPage.objects.live().filter(promoted=True)
  return {
    'page': page,
    'projects': projects,
  }


@register.inclusion_tag("freestyle/funders.html", takes_context=True)
def cgri_funders(context):
  '''
  This template tag is used to build the home page funder section.
  '''
  homepage = context['request'].site.root_page.specific
  funders = homepage.funders.all()
  primary_funders = funders[:3]
  other_funders = funders[3:]
  return {
    'funders': funders,
    'primary_funders': primary_funders,
    'other_funders': other_funders,
  }


@register.inclusion_tag("freestyle/recent_publications.html")
def cgri_recent_publications():
  '''
  This template tag is used to build the home page recent publications
  section.
  '''
  publications = PublicationPage.objects.live().order_by("-date")
  return {'publications': publications}


@register.inclusion_tag("freestyle/current_projects.html")
def cgri_current_projects():
  '''
  This template tag is used to build the home page current projects section
  '''
  projects = ProjectPage.objects.live().filter(promoted=True)
  return {'projects': projects}
