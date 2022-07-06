from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.country.models import Country
from apps.country.serializers.admin_serializer import CountrySerializer
from utils.CommonResultRenderer import CommonResultRenderer


class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)
