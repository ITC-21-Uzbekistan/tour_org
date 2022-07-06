from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from tourism_org.settings import DEFAULT_REQUEST_LANG
from utils.CommonResultRenderer import CommonResultRenderer
from apps.gallery.models import CategoryImage
from apps.gallery.serializers.client_serializer import CategoryImageSerializerForClient


class CategoryImageListAPIView(ListAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def list(self, request, *args, **kwargs):
        language = request.headers.get('language', DEFAULT_REQUEST_LANG)
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)


class CategoryImageRetrieveAPIView(RetrieveAPIView):
    queryset = CategoryImage.objects.all()
    serializer_class = CategoryImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def retrieve(self, request, *args, **kwargs):
        language = request.headers.get('language', DEFAULT_REQUEST_LANG)
        serializer = self.get_serializer(self.get_object(), context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)
