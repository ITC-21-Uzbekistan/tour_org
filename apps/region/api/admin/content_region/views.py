from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.region.models import ContentRegion
from apps.region.serializers.admin_serializer import ContentRegionSerializer
from utils.CommonResultRenderer import CommonResultRenderer


class ContentRegionListCreateAPIView(ListCreateAPIView):
    queryset = ContentRegion.objects.all()
    serializer_class = ContentRegionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)


class ContentRegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentRegion.objects.all()
    serializer_class = ContentRegionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)
