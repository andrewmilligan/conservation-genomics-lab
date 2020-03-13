from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class ImageLinkBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    url = blocks.URLBlock(required=False)

    class Meta:
        label = "Image links"
        icon = "image"
        template = "freestyle/blocks/image_link_column_block.html"
