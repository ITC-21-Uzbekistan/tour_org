from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from apps.region.models import Region
from apps.region.serializers import RegionWithContentSerializer


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionWithContentSerializer
    permission_classes = (AllowAny,)


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionWithContentSerializer
    permission_classes = (AllowAny,)
