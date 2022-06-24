from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from ..models import ContentRegion
from ..serializers import ContentRegionSerializer


class ContentRegionListCreateAPIView(ListCreateAPIView):
    queryset = ContentRegion.objects.all()
    serializer_class = ContentRegionSerializer
    permission_classes = (AllowAny,)


class ContentRegionRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentRegion.objects.all()
    serializer_class = ContentRegionSerializer
    permission_classes = (AllowAny,)
