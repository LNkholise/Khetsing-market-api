# Generated by Django 5.1.7 on 2025-04-10 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_listing_additional_info_markdown'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khetsinguser',
            name='phone_number',
            field=models.CharField(default='', max_length=15, unique=True),
        ),
    ]
