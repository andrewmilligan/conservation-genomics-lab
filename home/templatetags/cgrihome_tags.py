from django import template

from wagtail.core.models import Page
from articles.models import ProjectPage, PublicationPage

register = template.Library()


@register.inclusion_tag("home/carousel.html", takes_context=True)
def cgri_carousel(context):
    '''
    This template tag is used to build the home page carousel.
    '''
    page = context['page']
    projects = ProjectPage.objects.live()
    return {
            'page': page,
            'projects': projects,
            }


@register.inclusion_tag("home/funders.html", takes_context=True)
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


@register.inclusion_tag("home/recent_publications.html")
def cgri_recent_publications():
    '''
    This template tag is used to build the home page recent publications
    section.
    '''
    publications = PublicationPage.objects.live().order_by("-date")
    return {'publications': publications}


@register.inclusion_tag("home/current_projects.html")
def cgri_current_projects():
    '''
    This template tag is used to build the home page current projects section
    '''
    projects = ProjectPage.objects.live()
    return {'projects': projects}
