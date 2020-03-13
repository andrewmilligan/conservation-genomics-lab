from wagtail.core import blocks


class CGRIStyleBlock(blocks.ChoiceBlock):
    STYLES = (
        ('dark', 'Dark'),
        ('light', 'Light'),
    )

    def __init__(self, *args, **kwargs):
        super(CGRIStyleBlock, self).__init__(
            choices=self.STYLES,
            *args,
            **kwargs
        )
