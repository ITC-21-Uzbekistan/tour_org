from django.urls import path
from .api.views import ImageListAPIView, ImageRetrieveAPIView
from .api.image_view import ImageListCreateAPIView, ImageRetrieveUpdateDestroyAPIView
from .api.content_view import ContentImageListCreateAPIView, ContentImageRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('prod/', ImageListAPIView.as_view()),
    path('prod/<str:pk>/', ImageRetrieveAPIView.as_view()),

    path('content/', ContentImageListCreateAPIView.as_view()),
    path('content/<str:pk>/', ContentImageRetrieveUpdateDestroyAPIView.as_view()),

    path('image/', ImageListCreateAPIView.as_view()),
    path('image/<str:pk>/', ImageRetrieveUpdateDestroyAPIView.as_view()),
]
