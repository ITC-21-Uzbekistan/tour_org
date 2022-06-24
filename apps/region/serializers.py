from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Region, ContentRegion
from apps.gallery.serializers import ImageWithContentSerializer, ImageSerializerForUser


class ContentRegionSerializer(ModelSerializer):
    class Meta:
        model = ContentRegion
        fields = [
            'id',
            'region',
            'language',
            'region_name',
            'region_info'
        ]


class RegionWithContentSerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Region
        fields = [
            'id',
            'created_by',
            'created_at',
            'region_name',
            'region_url',
            'region_meta_keywords',
            'country',
            'region_images',
            'contents',
        ]

    def _get_contents(self, region):
        contents = ContentRegion.objects.filter(region=region)
        return ContentRegionSerializer(contents, many=True).data


class RegionSerializerForUser(ModelSerializer):
    region_name = SerializerMethodField('_get_region_name')
    region_info = SerializerMethodField('_get_region_info')
    region_images = SerializerMethodField('_get_region_images')

    class Meta:
        model = Region
        fields = [
            'id',
            'region_name',
            'region_info',
            'region_url',
            'region_meta_keywords',
            'region_images',
        ]

    def _get_region_images(self, region):
        return ImageSerializerForUser(region.region_images, many=True,
                                      context={'language': self.context.get('language')}).data

    def _get_region_name(self, region):
        return ContentRegion.objects.get(region=region, language_id=str(self.context.get('language'))).region_name

    def _get_region_info(self, region):
        return ContentRegion.objects.get(region=region, language_id=str(self.context.get('language'))).region_info
