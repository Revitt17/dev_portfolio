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
            'hr', 'link', 'code', 'blockquote']
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




