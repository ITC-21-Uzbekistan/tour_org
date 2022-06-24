# Generated by Django 4.0.5 on 2022-06-23 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gallery', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('is_delete', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('country_url', models.CharField(max_length=255)),
                ('country_meta_keywords', models.CharField(max_length=500)),
                ('country_images', models.ManyToManyField(db_table='country_images', related_name='country_images', to='gallery.image')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('deleted_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'country',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ContentCountry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('country_name', models.CharField(blank=True, max_length=255, null=True)),
                ('country_info', models.TextField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='country.country')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='language.language')),
            ],
            options={
                'db_table': 'content_country',
                'ordering': ['id'],
            },
        ),
    ]