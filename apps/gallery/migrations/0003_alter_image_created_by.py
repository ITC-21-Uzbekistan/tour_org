# Generated by Django 4.0.5 on 2022-07-02 08:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0002_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
