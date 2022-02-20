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