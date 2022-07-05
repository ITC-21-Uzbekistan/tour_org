from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.gallery.models import Image, ContentImage, CategoryImage, ContentCategoryImage


class ImageSerializerForClient(ModelSerializer):
    alt_text = SerializerMethodField('_get_alt_text')
    description = SerializerMethodField('_get_description')

    class Meta:
        model = Image
        fields = ['id', 'image', 'category', 'alt_text', 'description']

    def _get_alt_text(self, image):
        return ContentImage.objects.get(image=image, language_id=self.context.get('language')).alt_text

    def _get_description(self, image):
        return ContentImage.objects.get(image=image, language_id=self.context.get('language')).description


class CategoryImageSerializerForClient(ModelSerializer):
    category_name = SerializerMethodField('_get_category_name')

    class Meta:
        model = CategoryImage
        fields = ['id', 'category_name', 'category_image']

    def _get_category_name(self, category):
        return ContentCategoryImage.objects.get(category=category, language_id=self.context.get('language')).category_name
