from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.country.models import ContentCountry
from apps.country.serializers.admin_serializer import ContentCountrySerializer


class ContentCountryListCreateAPIView(ListCreateAPIView):
    queryset = ContentCountry.objects.all()
    serializer_class = ContentCountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ContentCountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentCountry.objects.all()
    serializer_class = ContentCountrySerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
