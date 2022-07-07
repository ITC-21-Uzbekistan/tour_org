from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.status import HTTP_200_OK

from apps.region.models import Region
from apps.region.serializers import RegionSerializerForUser


