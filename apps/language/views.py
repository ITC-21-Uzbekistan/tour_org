from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Language
from .serializers import LanguageSerializer
from utils.CommonResultRenderer import CommonResultRenderer


class ListCreateLanguageView(ListCreateAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)


class RetrieveUpdateDestroyLanguageView(RetrieveUpdateDestroyAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = (AllowAny,)
    renderer_classes = (CommonResultRenderer,)
