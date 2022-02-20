from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Contact


@modeladmin_register
class ContactAdmin(ModelAdmin):

    model = Contact
    menu_label = "Contact Form"
    menu_icon = "form"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("name", "email", "subject", "message")
    search_fields = ("name", "email", "subject", "message")
