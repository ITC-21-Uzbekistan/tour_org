from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from ..models import Image
from ..serializers import ImageWithContentSerializer


class ImageListCreateAPIView(ListCreateAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageWithContentSerializer
    permission_classes = (AllowAny,)


class ImageRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.filter(is_delete=False)
    serializer_class = ImageWithContentSerializer
    permission_classes = (AllowAny,)
