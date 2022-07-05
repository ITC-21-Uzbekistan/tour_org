from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from apps.gallery.models import Image
from apps.gallery.serializers.client_serializer import ImageSerializerForClient
from tourism_org.settings import DEFAULT_REQUEST_LANG
from utils.CommonResultRenderer import CommonResultRenderer


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def list(self, request, *args, **kwargs):

        language = request.headers.get('language', DEFAULT_REQUEST_LANG)
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)


class ImageRetrieveAPIView(RetrieveAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def retrieve(self, request, *args, **kwargs):

        language = request.headers.get('language', DEFAULT_REQUEST_LANG)
        serializer = self.get_serializer(self.get_object(), context={'language': str(language)})

        return Response(serializer.data, status=HTTP_200_OK)
