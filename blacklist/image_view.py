from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response

from utils.CommonResultRenderer import CommonResultRenderer
from utils.common_result import CommonResult
from apps.gallery.models import Image
from apps.gallery.serializers import ImageWithContentSerializer


class ImageListCreateAPIView(ListCreateAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageWithContentSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)

    def list(self, request, *args, **kwargs):
        result = CommonResult()

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data, context={'created_by': request.user})

        if not serializer.is_valid():
            print("This: ", serializer.errors)

            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        else:
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            return Response(result.get_response, status=status.HTTP_201_CREATED, headers=headers)


class ImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageWithContentSerializer
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
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'created_by': request.user})
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

        return Response(result.get_response, status=201)

    def destroy(self, request, *args, **kwargs):
        result = CommonResult()

        instance = self.get_object()
        instance.is_delete = True
        instance.deleted_by = request.user

        instance.save()

        result.set_response(
            success=True,
            status_code=204,
            message="SUCCESSFULLY DELETED",
            data=None
        )

        return Response(result.get_response, status=status.HTTP_204_NO_CONTENT)


