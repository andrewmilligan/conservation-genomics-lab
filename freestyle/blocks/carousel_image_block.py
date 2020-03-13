from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class CarouselImageBlock(blocks.StructBlock):
    image = ImageChooserBlock()
    title = blocks.CharBlock(max_length=200, required=False)
    blurb = blocks.RichTextBlock(required=False)
    page = blocks.PageChooserBlock(required=False)
    url = blocks.URLBlock(
        required=False,
        help_text="Ignored if page is set"
    )

    class Meta:
        label = "Carousel image"
        icon = "image"
