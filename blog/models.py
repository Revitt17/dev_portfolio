from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcodeblock.blocks import CodeBlock
from streams import blocks


class Blog(Page):

    template = "blog/blog_page.html"
    parent_page_types = ["home.HomePage"]
    subpage_types = []
    
    # Banner Section
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    # Post Section
    post_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    post_date = models.CharField(
        blank=False,
        null=True,
        max_length=50,
        help_text="yyyy.mm.dd"
    )
    post_author = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    
    
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('banner_image'),
        ], heading="Banner Section"),
        MultiFieldPanel([
            ImageChooserPanel('post_image'),
            FieldPanel('post_date'),
            FieldPanel('post_author'),
        ], heading="Post Section"),
    ]

