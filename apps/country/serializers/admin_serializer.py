from rest_framework.serializers import ModelSerializer, SerializerMethodField

from apps.country.models import ContentCountry, Country


class ContentCountrySerializer(ModelSerializer):
    class Meta:
        model = ContentCountry
        fields = "__all__"


class CountrySerializer(ModelSerializer):
    contents = SerializerMethodField('_get_contents')

    class Meta:
        model = Country
        fields = (
            'id',
            'country_name',
            'country_url',
            'country_meta_keywords',
            'country_images',
            'created_at',
            'created_by',
            'contents',
        )

    def _get_contents(self, country):
        contents = ContentCountry.objects.filter(country=country)
        return ContentCountrySerializer(contents, many=True).data
