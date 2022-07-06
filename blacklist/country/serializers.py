from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.country.models import Country, ContentCountry
from apps.gallery.serializers import ImageWithContentSerializer, ImageSerializerForUser


class ContentCountrySerializer(ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = [
            'id',
            'country',
            'language',
            'country_name',
            'country_info'
        ]


class CountryWithContentSerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Country
        fields = [
            'id',
            'created_by',
            'created_at',
            'country_name',
            'country_url',
            'country_meta_keywords',
            'country_images',
            'contents',
        ]

    def _get_contents(self, country):
        contents = ContentCountry.objects.filter(country=country)
        return ContentCountrySerializer(contents, many=True).data


class CountrySerializerForUser(ModelSerializer):
    country_name = SerializerMethodField('_get_country_name')
    country_info = SerializerMethodField('_get_country_info')
    country_images = SerializerMethodField('_get_country_images')

    class Meta:
        model = Country
        fields = [
            'id',
            'country_name',
            'country_info',
            'country_url',
            'country_meta_keywords',
            'country_images'
        ]

    def _get_country_images(self, country):
        return ImageSerializerForUser(country.country_images, many=True, context={'language': self.context.get('language')}).data

    def _get_country_name(self, country):
        return ContentCountry.objects.get(country=country, language_id=str(self.context.get('language'))).country_name

    def _get_country_info(self, country):
        return ContentCountry.objects.get(country=country, language_id=str(self.context.get('language'))).country_info
