from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required=True,
        help_text='Text to display',
    )

    class Meta:
        template = "streams/title_block.html"
        icon = "edit"
        label = "Title"


class TextBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(
        required=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', \
            'hr', 'link', 'code', 'blockquote', 'embed']
    )

    class Meta:
        template = "streams/text_block.html"
        icon = "edit"
        label = "Rich Text"


class ImageBlock(blocks.StructBlock):

    image = ImageChooserBlock()
    text = blocks.CharBlock(
        max_length=140, 
        required=False
    )

    class Meta:
        template = "streams/image_block.html"
        icon = "image"
        label = "Image"


class FrameBlock(blocks.StructBlock):

    src = blocks.URLBlock(
        required=True,
        blank=False,
        max_length=500,
    )
    width = blocks.CharBlock(
        required=True,
        blank=False,
        max_length=500,
    )
    height = blocks.CharBlock(
        required=True,
        blank=False,
        max_length=500,
    )
    frameborder = blocks.CharBlock(
        required=True,
        blank=False,
        max_length=500,
    )
    marginwidth = blocks.CharBlock(
        required=True,
        blank=False,
        max_length=500,
    )
    marginheight = blocks.CharBlock(
        required=True,
        blank=False,
        max_length=500,
    )

    class Meta:
        template = "streams/iframe_block.html"
        icon = "edit"
        label = "iFrame"
