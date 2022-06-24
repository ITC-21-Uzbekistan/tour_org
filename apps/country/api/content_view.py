from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from ..models import ContentCountry
from ..serializers import ContentCountrySerializer


class ContentCountryListCreateAPIView(ListCreateAPIView):
    queryset = ContentCountry.objects.all()
    serializer_class = ContentCountrySerializer
    permission_classes = (AllowAny,)


class ContentCountryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentCountry.objects.all()
    serializer_class = ContentCountrySerializer
    permission_classes = (AllowAny,)
