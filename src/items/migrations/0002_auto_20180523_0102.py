# Generated by Django 2.0.4 on 2018-05-23 01:02

from django.db import migrations, models
import items.models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image4',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='item',
            name='image5',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='item',
            name='image6',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field'),
        ),
    ]
