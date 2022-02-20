from wagtail.core import blocks


class HeaderBlock(blocks.StructBlock):

    text = blocks.CharBlock(
        required=True,
    )

    class Meta:
        template = "streams/header_block.html"
        icon = "edit"
        label = "Header"


class ParagrapherBlock(blocks.StructBlock):

    text = blocks.RichTextBlock(
        required=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', \
            'hr', 'link', 'image', 'code', 'blockquote']
    )

    class Meta:
        template = "streams/paragrapher_block.html"
        icon = "edit"
        label = "Paragraph"
