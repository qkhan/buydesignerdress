# Generated by Django 2.0.4 on 2018-05-18 00:38

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180518_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage1',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage2',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productImage3',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='product',
            name='productThumb',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=products.models.upload_location, width_field='width_field'),
        ),
    ]
