from django.urls import path

from apps.country.api.admin.content_country.views import ContentCountryListCreateAPIView, \
    ContentCountryRetrieveUpdateDestroyAPIView
from apps.country.api.admin.country.views import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    # FOR ADMIN
    path('admin/content-country/', ContentCountryListCreateAPIView.as_view()),
    path('admin/content-country/<str:pk>/', ContentCountryRetrieveUpdateDestroyAPIView.as_view()),

    path('admin/country/', CountryListCreateAPIView.as_view()),
    path('admin/country/<str:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view()),
]
