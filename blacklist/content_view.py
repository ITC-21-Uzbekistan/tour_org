from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from utils.CommonResultRenderer import CommonResultRenderer
from apps.gallery.models import ContentImage
from apps.gallery.serializers import ContentImageSerializer


class ContentImageListCreateAPIView(ListCreateAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)


class ContentImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)

