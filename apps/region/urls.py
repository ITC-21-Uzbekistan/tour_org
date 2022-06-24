from django.urls import path

from .api.views import RegionListAPIView, RegionRetrieveAPIView
from .api.content_view import ContentRegionListCreateAPIView, ContentRegionRetrieveUpdateDestroyAPIView
from .api.region_view import RegionListCreateAPIView, RegionRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('prod/', RegionListAPIView.as_view()),
    path('prod/<str:pk>/', RegionRetrieveAPIView.as_view()),

    path('content/', ContentRegionListCreateAPIView.as_view()),
    path('content/<str:pk>/', ContentRegionRetrieveUpdateDestroyAPIView.as_view()),

    path('region/', RegionListCreateAPIView.as_view()),
    path('region/<str:pk>/', RegionRetrieveUpdateDestroyAPIView.as_view()),
]
