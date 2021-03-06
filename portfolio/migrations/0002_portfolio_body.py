# Generated by Django 4.0.2 on 2022-02-17 03:01

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='body',
            field=wagtail.core.fields.StreamField([('header', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(required=True))])), ('paragraph', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'image', 'code', 'blockquote'], required=True))])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], null=True),
        ),
    ]
