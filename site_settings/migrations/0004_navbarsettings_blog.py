# Generated by Django 4.0.2 on 2022-02-28 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0003_rename_footer_footersettings_copyright_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='navbarsettings',
            name='blog',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
