import json
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from .models import Language
from .serializers import LanguageSerializer
from utils.common_result import CommonResult


class ListCreateLanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        result = CommonResult()

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)

        result.set_response(
            success=True,
            status_code=200,
            message='SUCCESS',
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
            message='SUCCESSFULLY CREATED',
            data=serializer.data
        )

        return Response(result.get_response, status=status.HTTP_201_CREATED, headers=headers)


class RetrieveUpdateDestroyLanguageView(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (AllowAny,)

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
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
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
        self.perform_destroy(instance)

        result.set_response(
            success=True,
            status_code=204,
            message="SUCCESSFULLY DELETED",
            data=None
        )

        return Response(result.get_response, status=status.HTTP_204_NO_CONTENT)
