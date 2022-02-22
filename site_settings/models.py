from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class NavbarSettings(BaseSetting):

    brand = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    home = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    about = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    work = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )
    contact = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )

    panels = [
        FieldPanel("brand"),
        FieldPanel("home"),
        FieldPanel("about"),
        FieldPanel("work"),
        FieldPanel("contact"),
    ]


@register_setting
class FooterSettings(BaseSetting):

    footer = models.CharField(
        max_length=50,
        blank=False,
        null=True,
    )

    panels = [
        FieldPanel("footer"),
    ]


@register_setting
class PortfolioSettings(BaseSetting):

    banner_home_slug = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text="word 'home' in portfolio_banner_section.html",
    )
    project_info = models.CharField(
        blank=False,
        null=True,
        max_length=50,
        help_text="word 'Project_info' in portfolio_project_info_section.html",
    )
    project_info_category = models.CharField(
        blank=False,
        null=True,
        max_length=50,
        help_text="word 'Category' in portfolio_project_info_section.html",
    )
    project_info_client = models.CharField(
        blank=True,
        max_length=50,
        help_text="word 'Client' in portfolio_project_info_section.html",
    )
    project_info_project_date = models.CharField(
        blank=False,
        null=True,
        max_length=50,
        help_text="word 'Project date' in portfolio_project_info_section.html",
    )
    project_info_project_url = models.CharField(
        blank=True,
        max_length=50,
        help_text="word 'Project URL' in portfolio_project_info_section.html",
    )
    project_info_website_button = models.CharField(
        blank=True,
        max_length=50,
        help_text="word 'Website' in portfolio_project_info_section.html",
    )
    project_info_github_button = models.CharField(
        blank=True,
        max_length=50,
        help_text="word 'GitHub' in portfolio_project_info_section.html",
    )

    panels = [
        FieldPanel("banner_home_slug"),
        FieldPanel("project_info"),
        FieldPanel("project_info_category"),
        FieldPanel("project_info_client"),
        FieldPanel("project_info_project_date"),
        FieldPanel("project_info_project_url"),
        FieldPanel("project_info_website_button"),
        FieldPanel("project_info_github_button"),
    ]


@register_setting
class BlogSettings(BaseSetting):

    banner_home_slug = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text="word 'home' in blog_banner_section.html"
    )
    post_posted = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text="word 'posted' in blog_post_section.html"
    )
    post_by = models.CharField(
        max_length=50,
        blank=False,
        null=True,
        help_text="word 'by' in blog_post_section.html"
    )
    post_related_articles = models.CharField(
        blank=False,
        null=True,
        max_length=50,
        help_text="word 'Related articles' in blog_post_section.html"
    )

    panels = [
        FieldPanel("banner_home_slug"),
        FieldPanel("post_posted"),
        FieldPanel("post_by"),
        FieldPanel("post_related_articles"),
    ]