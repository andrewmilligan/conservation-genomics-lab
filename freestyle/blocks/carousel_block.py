from wagtail.core import blocks
from .carousel_image_block import CarouselImageBlock


class CarouselBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    images = blocks.ListBlock(CarouselImageBlock())

    class Meta:
        label = "Carousel"
        template = 'freestyle/blocks/carousel.html'
        icon = 'image'
