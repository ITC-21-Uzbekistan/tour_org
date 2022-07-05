from rest_framework.serializers import ModelSerializer, SerializerMethodField, raise_errors_on_nested_writes, UUIDField
from rest_framework.utils import model_meta
import traceback

from apps.gallery.models import Image, ContentImage, CategoryImage


class ContentImageSerializer(ModelSerializer):

    class Meta:
        model = ContentImage
        fields = ['id', 'language', 'image', 'alt_text', 'description']


class CategoryImageSerializer(ModelSerializer):
    class Meta:
        model = CategoryImage
        fields = "__all__"


class ImageWithContentSerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Image
        fields = ['id', 'image', 'created_at', 'created_by', 'contents']

    # override create method of serializer. This will get user as context and creates image
    def create(self, validated_data):
        instance = Image.objects.create(**validated_data, created_by=self.context.get('created_by'))

        return instance

    # override update method of serializer. This will get user as context and updates image
    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        info = model_meta.get_field_info(instance)

        m2m_fields = []
        for attr, value in validated_data.items():
            if attr in info.relations and info.relations[attr].to_many:
                m2m_fields.append((attr, value))
            else:
                setattr(instance, attr, value)

        # gets user from context and saves
        instance.created_by = self.context.get('created_by')
        instance.save()

        for attr, value in m2m_fields:
            field = getattr(instance, attr)
            field.set(value)

        return instance

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
