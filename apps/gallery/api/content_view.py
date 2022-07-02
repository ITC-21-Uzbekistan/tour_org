from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from utils.common_result import CommonResult
from ..models import ContentImage
from ..serializers import ContentImageSerializer


class ContentImageListCreateAPIView(ListCreateAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

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

        return Response(result.get_response, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        result = CommonResult()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        result.set_response(
            success=True,
            status_code=201,
            message="SUCCESSFULLY CREATED",
            data=serializer.data
        )

        return Response(result.get_response, status=status.HTTP_201_CREATED, headers=headers)


class ContentImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def retrieve(self, request, *args, **kwargs):
        result = CommonResult()

        instance = self.get_object()
        serializer = self.get_serializer(instance)

        result.set_response(
            success=True,
            status_code=200,
            message="SUCCESS",
            data=serializer.data
        )

        return Response(result.get_response, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        result = CommonResult()

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        result.set_response(
            success=True,
            status_code=201,
            message="SUCCESSFULLY UPDATED",
            data=serializer.data
        )

        return Response(result.get_response, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        result = CommonResult()

        instance = self.get_object()
        self.perform_destroy(instance)

        result.set_response(
            success=True,
            status_code=204,
            message="SUCCESSFULLY DELETED",
            data=None
        )

        return Response(result.get_response, status=status.HTTP_204_NO_CONTENT)
