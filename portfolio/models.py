from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcodeblock.blocks import CodeBlock

from streams import blocks


class Portfolio(Page):

    template = "portfolio/portfolio_page.html"
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
    home_slug = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )

    # Project Info Section
    cover_image_project = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    project_info = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    category_title = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    category = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    client_title = models.CharField(
        blank=True,
        max_length=50,
    )
    client = models.CharField(
        blank=True,
        max_length=50,
    )
    project_date_title = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    project_date = models.CharField(
        blank=False,
        max_length=50,
    )
    project_url_title = models.CharField(
        blank=True,
        max_length=50,
    )
    project_url = models.URLField(
        blank=True,
        max_length=50,
    )
    website_button = models.CharField(
        blank=True,
        max_length=50,
    )
    website_button_url = models.URLField(
        blank=True,
        max_length=50,
    )
    github_button = models.CharField(
        blank=True,
        max_length=50,
    )
    github_button_url = models.URLField(
        blank=True,
        max_length=50,
    )
    body = StreamField([
        ("header", blocks.HeaderBlock()),
        ("paragraph", blocks.ParagrapherBlock()),
        ("code", CodeBlock(label=("Code"))),
    ], null=True, blank=False)
    
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('banner_image'),
            FieldPanel('home_slug'),
        ], heading="Banner Section"),
        MultiFieldPanel([
            ImageChooserPanel('cover_image_project'),
            FieldPanel('project_info'),
            FieldPanel('category_title'),
            FieldPanel('category'),
            FieldPanel('client_title'),
            FieldPanel('client'),
            FieldPanel('project_date_title'),
            FieldPanel('project_date'),
            FieldPanel('project_url_title'),
            FieldPanel('project_url'),
            FieldPanel('website_button'),
            FieldPanel('website_button_url'),
            FieldPanel('github_button'),
            FieldPanel('github_button_url'),
        ], heading="Project Info Section"),
        StreamFieldPanel("body")
    ]
