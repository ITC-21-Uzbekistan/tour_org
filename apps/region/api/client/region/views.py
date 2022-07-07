from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from apps.region.models import Region
from apps.region.serializers.client_serializer import RegionSerializerForClient
from utils.CommonResultRenderer import CommonResultRenderer


class RegionListAPIView(ListAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionSerializerForClient
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def list(self, request, *args, **kwargs):
        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)


class RegionRetrieveAPIView(RetrieveAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionSerializerForClient
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_object(), context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)