from django.db import models
from wagtail.snippets.models import register_snippet


@register_snippet
class Contact(models.Model):

    id = models.AutoField(primary_key=True,)
    
    name = models.CharField(
        max_length=30,
        null=True,
    )
    email = models.EmailField(
        max_length=255,
        null=True,
    )
    subject = models.CharField(
        max_length=255,
        null=True,
    )
    message = models.TextField(
        null=True,
    )
