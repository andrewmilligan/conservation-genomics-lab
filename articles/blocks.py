from __future__ import absolute_import, unicode_literals

from wagtail.wagtailcore import blocks
from wagtail.wagtailimages.blocks import ImageChooserBlock


## CaptionedImageBlock
#
#  This is a block (to be used in stream fields) that defines a captioned
#  image. In addition to an actual image, this image block may have title
#  information, caption information, credit information, etc.
#
class CaptionedImageBlock(blocks.StructBlock):
  image = ImageChooserBlock()
  title = blocks.CharBlock(null=True, required=False)
  subtitle = blocks.CharBlock(null=True, required=False)
  caption = blocks.RichTextBlock(null=True, required=False)
  credit = blocks.CharBlock(null=True, required=False)
  max_width = blocks.IntegerBlock(null=True, required=False,
      min_value=0, help_text="maximum width of image in pixels")

  class Meta:
    template = 'articles/blocks/captioned_image_block.html'
    icon = 'image'


## AuthorBlock
#
#  This is a block (to be used in stream fields) that defines an author for a
#  publication.
#
class AuthorBlock(blocks.StructBlock):
  name = blocks.CharBlock()
  institution = blocks.CharBlock(null=True, required=False)

  class Meta:
    label = "Author"
    template = 'articles/blocks/author_block.html'
    icon = 'user'
