from django.urls import path

from .api.views import CountryListAPIView, CountryRetrieveAPIView
from .api.content_view import ContentCountryListCreateAPIView, ContentCountryRetrieveUpdateDestroyAPIView
from .api.country_view import CountryListCreateAPIView, CountryRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('prod/', CountryListAPIView.as_view()),
    path('prod/<str:pk>/', CountryRetrieveAPIView.as_view()),

    path('content/', ContentCountryListCreateAPIView.as_view()),
    path('content/<str:pk>/', ContentCountryRetrieveUpdateDestroyAPIView.as_view()),

    path('country/', CountryListCreateAPIView.as_view()),
    path('country/<str:pk>/', CountryRetrieveUpdateDestroyAPIView.as_view())
]
