from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


class CaptionedImageBlock(blocks.StructBlock):
  image = ImageChooserBlock()
  title = blocks.CharBlock(null=True, required=False)
  subtitle = blocks.CharBlock(null=True, required=False)
  caption = blocks.RichTextBlock(null=True, required=False)
  credit = blocks.CharBlock(null=True, required=False)

  class Meta:
    template = 'projects/blocks/captioned_image_block.html'
    icon = 'image'
