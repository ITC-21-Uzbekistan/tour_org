from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from rest_framework.utils import model_meta

from apps.gallery.models import ContentImage, CategoryImage, Image, ContentCategoryImage


class ContentImageSerializer(ModelSerializer):
    class Meta:
        model = ContentImage
        fields = ('id', 'language', 'image', 'alt_text', 'description')


class ContentCategoryImageSerializer(ModelSerializer):
    class Meta:
        model = ContentCategoryImage
        fields = "__all__"


class CategoryImageSerializer(ModelSerializer):
    category_name = SerializerMethodField('_get_contents')

    class Meta:
        model = CategoryImage
        fields = ('id', 'category_name', 'category_image')

    def _get_contents(self, category):
        contents = ContentCategoryImage.objects.filter(category=category)
        return ContentCategoryImageSerializer(contents, many=True)


class ImageWithContentSerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Image
        fields = ('id', 'image', 'category', 'created_at', 'created_by', 'contents')

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
