from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from apps.region.models import Region
from apps.region.serializers.admin_serializer import RegionSerializerWithContent
from utils.CommonResultRenderer import CommonResultRenderer


class RegionListCreateAPIView(ListCreateAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionSerializerWithContent
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'created_by': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.filter(is_delete=False)
    serializer_class = RegionSerializerWithContent
    permission_classes = (IsAuthenticatedOrReadOnly,)
    renderer_classes = (CommonResultRenderer,)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial, context={'created_by': request.user})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.is_delete = True
        instance.deleted_by = request.user

        instance.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

