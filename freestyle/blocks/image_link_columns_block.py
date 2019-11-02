from wagtail.core import blocks
from .image_link_block import ImageLinkBlock
from .cgri_style_block import CGRIStyleBlock


class ImageLinkColumnsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    image_links = blocks.ListBlock(ImageLinkBlock())
    style = CGRIStyleBlock(default='light')

    @property
    def column_class(self):
        n = len(self.image_links)
        if 12 % n == 0:
            return f'col-md-{12 / n}'
        else:
            return 'col-md-2'

    class Meta:
        label = "Image links"
        template = 'freestyle/blocks/image_link_columns.html'
        icon = 'link'
