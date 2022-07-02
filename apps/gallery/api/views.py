from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from utils.common_result import CommonResult
from ..models import Image
from ..serializers import ImageSerializerForUser


class ImageListAPIView(ListAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageSerializerForUser
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        result = CommonResult()

        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'language': language})

        result.set_response(
            success=True,
            status_code=200,
            message="SUCCESS",
            data=serializer.data
        )

        return Response(result.get_response, status=HTTP_200_OK)


class ImageRetrieveAPIView(RetrieveAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageSerializerForUser
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        result = CommonResult()

        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_object(), context={'language': str(language)})

        result.set_response(
            success=True,
            status_code=200,
            message="SUCCESS",
            data=serializer.data
        )

        return Response(result.get_response, status=HTTP_200_OK)
