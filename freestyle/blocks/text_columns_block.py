from wagtail.core import blocks
from .cgri_style_block import CGRIStyleBlock
from .text_column_block import TextColumnBlock


class TextColumnsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    columns = blocks.ListBlock(TextColumnBlock())
    style = CGRIStyleBlock(default='light')

    class Meta:
        label = "Text columns"
        template = "freestyle/blocks/text_columns_block.html"
        icon = "pilcrow"
