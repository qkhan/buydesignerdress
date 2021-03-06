# Generated by Django 2.0.4 on 2018-05-24 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('items', '0002_auto_20180523_0102'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['-timestamp', '-updated']},
        ),
        migrations.RenameField(
            model_name='item',
            old_name='updateDate',
            new_name='updated',
        ),
        migrations.AddField(
            model_name='item',
            name='added_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_add', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='item',
            name='last_edited_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_edit', to=settings.AUTH_USER_MODEL),
        ),
    ]
