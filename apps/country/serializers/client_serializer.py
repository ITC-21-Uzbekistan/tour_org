from rest_framework.serializers import ModelSerializer

from apps.country.models import Country


class CountryClientSerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'country_name',
            'country_url',
            'country_meta_keywords',
            'country_images',
            'created_info',
        )
