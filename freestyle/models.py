from __future__ import absolute_import, unicode_literals

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from freestyle.blocks import (
  CarouselBlock,
  ImageLinkColumnsBlock,
  TextColumnsBlock,
  RecentPublicationsBlock,
  CurrentProjectsBlock,
)


class FreestylePage(Page):
  body = StreamField([
    ('carousel', CarouselBlock()),
    ('image_link_columns', ImageLinkColumnsBlock()),
    ('text_columns', TextColumnsBlock()),
    ('recent_publications', RecentPublicationsBlock()),
    ('current_projects', CurrentProjectsBlock()),
  ])

  content_panels = Page.content_panels + [
    StreamFieldPanel('body'),
  ]
