# Generated by Django 4.0.2 on 2022-02-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('subject', models.CharField(max_length=255, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
    ]
