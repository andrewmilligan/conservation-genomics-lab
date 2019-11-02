from wagtail.core import blocks
from .cgri_style_block import CGRIStyleBlock


class CurrentProjectsBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    style = CGRIStyleBlock(default='light')

    class Meta:
        label = "Current projects"
        template = "freestyle/blocks/current_projects.html"
        icon = "list-ul"
