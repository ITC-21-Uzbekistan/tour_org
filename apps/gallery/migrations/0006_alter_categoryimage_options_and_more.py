# Generated by Django 4.0.5 on 2022-07-06 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_remove_categoryimage_category_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoryimage',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='contentcategoryimage',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelTable(
            name='categoryimage',
            table='category_image',
        ),
        migrations.AlterModelTable(
            name='contentcategoryimage',
            table='content_category_image',
        ),
    ]