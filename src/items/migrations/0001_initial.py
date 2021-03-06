# Generated by Django 2.0.4 on 2018-05-21 02:55

from django.db import migrations, models
import django.db.models.deletion
import items.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('sku', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=120)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('cartDesc', models.CharField(blank=True, max_length=120, null=True)),
                ('shortDesc', models.CharField(blank=True, max_length=250, null=True)),
                ('longDesc', models.TextField(blank=True, null=True)),
                ('thumb', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field')),
                ('image1', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field')),
                ('image2', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field')),
                ('image3', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=items.models.upload_location, width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('updateDate', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('stock', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('live', models.BooleanField(default=False)),
                ('itemLimited', models.BooleanField(default=False)),
                ('location', models.CharField(blank=True, max_length=250, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=True)),
                ('categoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.Category')),
            ],
            options={
                'ordering': ['-timestamp', '-updateDate'],
            },
        ),
        migrations.CreateModel(
            name='itemOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionPriceIncrement', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('itemId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_for_option', to='items.Item')),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionName', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='OptionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('optionGroupName', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='option',
            name='optionGroupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.OptionGroup'),
        ),
        migrations.AddField(
            model_name='itemoptions',
            name='optionGroupId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_for_option', to='items.OptionGroup'),
        ),
        migrations.AddField(
            model_name='itemoptions',
            name='optionID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='option_for_item', to='items.Option'),
        ),
    ]
