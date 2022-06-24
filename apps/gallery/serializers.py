from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Image, ContentImage


class ContentImageSerializer(ModelSerializer):
    class Meta:
        model = ContentImage
        fields = ['id', 'language', 'image', 'alt_text', 'description']


class ImageOnlySerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class ImageWithContentSerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Image
        fields = ['id', 'image', 'created_at', 'created_by', 'contents']

    def _get_contents(self, image):
        contents = ContentImage.objects.filter(image=image)
        return ContentImageSerializer(contents, many=True).data


class ImageSerializerForUser(ModelSerializer):
    alt_text = SerializerMethodField('_get_alt_text')
    description = SerializerMethodField('_get_description')

    class Meta:
        model = Image
        fields = ['id', 'image', 'alt_text', 'description']

    def _get_alt_text(self, image):
        return ContentImage.objects.get(image=image, language_id=self.context.get('language')).alt_text

    def _get_description(self, image):
        return ContentImage.objects.get(image=image, language_id=self.context.get('language')).description
