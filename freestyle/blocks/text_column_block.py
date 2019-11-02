from wagtail.core import blocks


class TextColumnBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=200, required=False)
    text = blocks.RichTextBlock(required=False)

    class Meta:
        label = "Text column"
        icon = "pilcrow"
