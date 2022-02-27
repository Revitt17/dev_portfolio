from django.db import models
from django.shortcuts import render
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
    body = StreamField([
        ("title", blocks.TitleBlock()),
        ("text", blocks.TextBlock()),
        ("image", blocks.ImageBlock()),
        ("code", CodeBlock(label=("Code"))),
    ], null=True, blank=False)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('banner_image'),
        ], heading="Banner Section"),
        MultiFieldPanel([
            ImageChooserPanel('post_image'),
            FieldPanel('post_date'),
            FieldPanel('post_author'),
        ], heading="Post Section"),
        StreamFieldPanel("body")
    ]

    def serve(self, request, *args, **kwargs):

        context = super().get_context(request, *args, **kwargs)
        context['blog'] = Blog.objects.live().public() 
        return render(request, 'blog/blog_page.html', context)
