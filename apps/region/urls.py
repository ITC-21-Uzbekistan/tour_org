from django.urls import path

from apps.region.api.admin.content_region.views import ContentRegionListCreateAPIView, \
    ContentRegionRetrieveUpdateDestroyAPIView
from apps.region.api.admin.region.views import RegionListCreateAPIView, RegionRetrieveUpdateDestroyAPIView
from apps.region.api.client.region.views import RegionListAPIView, RegionRetrieveAPIView

urlpatterns = [
    # ------------FOR CLIENTS------------

    # region list and retrieve for clients
    path('client/region/', RegionListAPIView.as_view()),
    path('client/region/<str:pk>/', RegionRetrieveAPIView.as_view()),

    # ------------FOR ADMIN------------

    # content of region list and retrieve for admin
    path('admin/content-region/', ContentRegionListCreateAPIView.as_view()),
    path('admin/content-region/<str:pk>/', ContentRegionRetrieveUpdateDestroyAPIView.as_view()),

    # region list and retrieve for admin
    path('admin/region/', RegionListCreateAPIView.as_view()),
    path('admin/region/<str:pk>/', RegionRetrieveUpdateDestroyAPIView.as_view()),
]
