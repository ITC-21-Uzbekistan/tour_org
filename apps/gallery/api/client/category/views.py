from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny

from utils.CommonResultRenderer import CommonResultRenderer
from apps.gallery.models import CategoryImage
from apps.gallery.serializers.client_serializer import CategoryImageSerializerForClient


class CategoryImageListAPIView(ListAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)


class CategoryImageRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)
