from wagtail.core import blocks
from .cgri_style_block import CGRIStyleBlock


class PageIndexBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    style = CGRIStyleBlock(default='light')
    pages = blocks.ListBlock(blocks.PageChooserBlock())

    class Meta:
        label = "Page index"
        template = "freestyle/blocks/page_index_block.html"
        icon = "list-ul"
