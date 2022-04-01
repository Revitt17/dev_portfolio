# Generated by Django 4.0.3 on 2022-04-01 19:57

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_alter_portfolio_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='body',
            field=wagtail.core.fields.StreamField([('title', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to display', required=True))])), ('text', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'code', 'blockquote', 'embed'], required=True))])), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('text', wagtail.core.blocks.CharBlock(max_length=140, required=False))])), ('iframe', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(blank=True, help_text='iframe', max_length=500, required=False))])), ('code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('css', 'CSS'), ('diff', 'diff'), ('html', 'HTML'), ('javascript', 'Javascript'), ('json', 'JSON'), ('python', 'Python'), ('scss', 'SCSS'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code'))], null=True),
        ),
    ]
