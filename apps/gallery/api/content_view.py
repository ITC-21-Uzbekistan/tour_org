from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from ..models import ContentImage
from ..serializers import ContentImageSerializer


class ContentImageListCreateAPIView(ListCreateAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (AllowAny,)


class ContentImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ContentImage.objects.all()
    serializer_class = ContentImageSerializer
    permission_classes = (AllowAny,)
