from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.country.models import Country
from apps.country.serializers.client_serializer import CountryClientSerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryClientSerializer



class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryClientSerializer