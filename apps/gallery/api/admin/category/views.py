from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.gallery.models import CategoryImage
from apps.gallery.serializers.admin_serializer import CategoryImageWithContentSerializer
from utils.CommonResultRenderer import CommonResultRenderer


class CategoryImageListCreateAPIView(ListCreateAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageWithContentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)


class CategoryImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageWithContentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)

