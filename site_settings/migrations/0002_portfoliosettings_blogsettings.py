# Generated by Django 4.0.2 on 2022-02-22 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_home_slug', models.CharField(help_text="word 'home' in portfolio_banner_section.html", max_length=50, null=True)),
                ('project_info', models.CharField(help_text="word 'Project_info' in portfolio_project_info_section.html", max_length=50, null=True)),
                ('project_info_category', models.CharField(help_text="word 'Category' in portfolio_project_info_section.html", max_length=50, null=True)),
                ('project_info_client', models.CharField(blank=True, help_text="word 'Client' in portfolio_project_info_section.html", max_length=50)),
                ('project_info_project_date', models.CharField(help_text="word 'Project date' in portfolio_project_info_section.html", max_length=50, null=True)),
                ('project_info_project_url', models.CharField(blank=True, help_text="word 'Project URL' in portfolio_project_info_section.html", max_length=50)),
                ('project_info_website_button', models.CharField(blank=True, help_text="word 'Website' in portfolio_project_info_section.html", max_length=50)),
                ('project_info_github_button', models.CharField(blank=True, help_text="word 'GitHub' in portfolio_project_info_section.html", max_length=50)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BlogSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_home_slug', models.CharField(help_text="word 'home' in blog_banner_section.html", max_length=50, null=True)),
                ('post_posted', models.CharField(help_text="word 'posted' in blog_post_section.html", max_length=50, null=True)),
                ('post_by', models.CharField(help_text="word 'by' in blog_post_section.html", max_length=50, null=True)),
                ('post_related_articles', models.CharField(help_text="word 'Related articles' in blog_post_section.html", max_length=50, null=True)),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]