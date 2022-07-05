from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Image, CategoryImage, ContentImage, ContentCategoryImage


@admin.register(Image)
class ImageAdmin(ModelAdmin):
    list_display = ('id', 'image', 'category')


@admin.register(CategoryImage)
class CategoryImageAdmin(ModelAdmin):
    list_display = ('id', 'category_image')


@admin.register(ContentImage)
class ContentImageAdmin(ModelAdmin):
    list_display = ('id', 'image', 'language', 'alt_text', 'description')


@admin.register(ContentCategoryImage)
class ContentCategoryImageAdmin(ModelAdmin):
    list_display = ('id', 'language', 'category_name')
