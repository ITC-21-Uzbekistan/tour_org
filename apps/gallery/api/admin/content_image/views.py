from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.gallery.models import ContentImage
from apps.gallery.serializers.admin_serializer import ContentImageSerializer
from utils.CommonResultRenderer import CommonResultRenderer


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
