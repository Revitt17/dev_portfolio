from django.db import models
from django.shortcuts import render
from wagtail.core.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from portfolio.models import Portfolio
from blog.models import Blog


class HomePage(Page):

    template = "home/home_page.html"
    parent_page_types = ["wagtailcore.Page"]
    subpage_types = ["portfolio.Portfolio", "blog.Blog"]
    max_count = 1
    
    # Hero Section
    hero_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    hero_lead_text = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    hero_typed_text = models.CharField(
        max_length=140,
        blank=False,
        null=True,
        help_text='Typed text, separate words with commas (,)',
    )
    hero_github_link = models.URLField(
        max_length=200,
        blank=True,
    )
    hero_linkedin_link = models.URLField(
        max_length=200,
        blank=True,
    )

    # About Section
    about_profile_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text="Vertical profile image 3x2 aspect ratio",
        on_delete= models.SET_NULL,
    )
    about_title = models.CharField(
        max_length=140,
        null=True,
        blank=False,
    )
    about_first_paragrapher = models.TextField(
        blank=False,
        null=True,
        max_length=500,
    )
    about_second_paragrapher = models.TextField(
        blank=True,
        null=True,
        max_length=500,
    )
    about_third_paragrapher = models.TextField(
        blank=True,
        null=True,
        max_length=500,
    )
    about_title_skills_subsection = models.CharField(
        max_length=140,
        null=True,
        blank=False,
    )

    # Work Section
    work_title = models.CharField(
        max_length=140,
        blank=False,
        null=True,
    )
    work_lead_text = models.TextField(
        blank=True,
        max_length=500,
    )

    # Contact Section
    contact_bg_img = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
    )
    contact_get_in_touch = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    contact_paragrapher = models.TextField(
        blank=False,
        null=True,
        max_length=500,
    )
    contact_address = models.CharField(
        blank=False,
        null=True,
        max_length=100,
    )
    contact_phone = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    contact_email = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    contact_send_a_message = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )
    contact_send_button = models.CharField(
        blank=False,
        null=True,
        max_length=50,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel("hero_background_image"),
            FieldPanel("hero_lead_text"),
            FieldPanel("hero_typed_text"),
            FieldPanel("hero_github_link"),
            FieldPanel("hero_linkedin_link"),
        ], heading="Hero Section"),
        MultiFieldPanel([
            ImageChooserPanel("about_profile_image"),
            FieldPanel("about_title"),
            FieldPanel("about_first_paragrapher"),
            FieldPanel("about_second_paragrapher"),
            FieldPanel("about_third_paragrapher"),
            FieldPanel("about_title_skills_subsection"),
            InlinePanel(
                "logos", 
                max_num=200, 
                min_num=1, 
                label="Logos"
            ),
        ], heading="About Section"),
        MultiFieldPanel([
            FieldPanel("work_title"),
            FieldPanel("work_lead_text"),
        ], heading="Work Section"),
        MultiFieldPanel([
            ImageChooserPanel("contact_bg_img"),
            FieldPanel('contact_get_in_touch'),
            FieldPanel('contact_paragrapher'),
            FieldPanel('contact_address'),
            FieldPanel('contact_phone'),
            FieldPanel('contact_email'),
            FieldPanel('contact_send_a_message'),
            FieldPanel('contact_send_button'),
        ], heading="Contact Section"),
    ]


    def serve(self, request, *args, **kwargs):
        """
        Use 'forms' from django standard for contact form in homepage.
        """
        from contact.forms import ContactForm

        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                instance = form.save()
                context = {'page': self, 'instance': instance}
                return render(
                    request, 'contact/contact_thankyou.html', context)
        else:
            form = ContactForm()

        context_contact = {'page': self, 'form': form}
        """
        Get context from 'Portfolio' necessary for 'home_work_section'.
        """
        context_portfolio = super().get_context(request, *args, **kwargs)
        context_portfolio['portfolio'] = Portfolio.objects.live().public()  
        """
        Get context from 'Blog' necessary for 'home_blog_section'.
        """ 
        context_blog = super().get_context(request, *args, **kwargs)
        context_blog['blog'] = Blog.objects.live().public() 
        """
        Merge context and view all.
        """
        #context = context_contact | context_portfolio | context_blog
        context = {**context_contact, **context_portfolio, **context_blog}
        return render(request, 'home/home_page.html', context)

    
class SkillLogos(Orderable):

    id = models.AutoField(primary_key=True)

    page = ParentalKey(
        HomePage, 
        on_delete=models.CASCADE,
        related_name='logos'
    )
    image = models.ForeignKey(
        'wagtailimages.Image',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
