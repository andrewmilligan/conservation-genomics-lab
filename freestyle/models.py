from __future__ import absolute_import, unicode_literals

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel

from freestyle.blocks import (
  CarouselBlock,
  ColumnsBlock,
  PageIndexBlock,
)


class FreestylePage(Page):
  body = StreamField([
    ('carousel', CarouselBlock()),
    ('columns', ColumnsBlock()),
    ('pages', PageIndexBlock()),
  ])

  content_panels = Page.content_panels + [
    StreamFieldPanel('body'),
  ]
