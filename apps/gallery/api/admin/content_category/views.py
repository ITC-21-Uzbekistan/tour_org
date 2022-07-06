from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.gallery.models import ContentCategoryImage
from apps.gallery.serializers.admin_serializer import ContentCategoryImageSerializer
from utils.CommonResultRenderer import CommonResultRenderer


class ContentCategoryImageListCreateAPIView(ListCreateAPIView):
    queryset = ContentCategoryImage.objects.all()
    serializer_class = ContentCategoryImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)


class ContentCategoryImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentCategoryImage.objects.all()
    serializer_class = ContentCategoryImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)
