from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from apps.country.models import Country
from apps.country.serializers import CountrySerializerForUser


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializerForUser
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_queryset(), many=True, context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)


class CountryRetrieveAPIView(RetrieveAPIView):
    queryset = Country.objects.filter(is_delete=False)
    serializer_class = CountrySerializerForUser
    permission_classes = (AllowAny,)

    def retrieve(self, request, *args, **kwargs):
        language = request.headers.get('language', 'd664a42d-abb2-47cf-8aa0-fcec9b0fcc9e')
        serializer = self.get_serializer(self.get_object(), context={'language': language})

        return Response(serializer.data, status=HTTP_200_OK)
