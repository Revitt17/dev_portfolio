# Generated by Django 4.0.2 on 2022-02-22 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_portfolio_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio',
            name='category_title',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='client_title',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='github_button',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='home_slug',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='project_date_title',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='project_info',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='project_url_title',
        ),
        migrations.RemoveField(
            model_name='portfolio',
            name='website_button',
        ),
    ]