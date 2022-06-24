from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from ..models import Country
from ..serializers import CountryWithContentSerializer


class CountryListCreateAPIView(ListCreateAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountryWithContentSerializer
    permission_classes = (AllowAny,)


class CountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountryWithContentSerializer
    permission_classes = (AllowAny,)
