# Generated by Django 5.1.7 on 2025-04-03 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images/'),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_4',
            field=models.ImageField(blank=True, null=True, upload_to='listing_images/'),
        ),
    ]
