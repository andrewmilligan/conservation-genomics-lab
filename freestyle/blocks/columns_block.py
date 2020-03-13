from wagtail.core import blocks
from .cgri_style_block import CGRIStyleBlock
from .text_column_block import TextColumnBlock
from .image_link_block import ImageLinkBlock


class ColumnsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    style = CGRIStyleBlock(default='light')
    columns = blocks.StreamBlock([
        ('text', TextColumnBlock()),
        ('image', ImageLinkBlock()),
    ])

    class Meta:
        label = "Columns"
        template = "freestyle/blocks/columns_block.html"
        icon = "form"
