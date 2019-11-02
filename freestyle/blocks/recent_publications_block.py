from wagtail.core import blocks
from .cgri_style_block import CGRIStyleBlock


class RecentPublicationsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    style = CGRIStyleBlock(default='light')

    class Meta:
        label = "Recent publications"
        template = "freestyle/blocks/recent_publications.html"
        icon = "list-ul"
