from django.urls import path
from apps.gallery.api.admin.category.views import CategoryImageListCreateAPIView, \
    CategoryImageRetrieveUpdateDestroyAPIView
from apps.gallery.api.admin.content_category.views import ContentCategoryImageListCreateAPIView, \
    ContentCategoryImageRetrieveUpdateDestroyAPIView
from apps.gallery.api.admin.content_image.views import ContentImageListCreateAPIView, \
    ContentImageRetrieveUpdateDestroyAPIView
from apps.gallery.api.admin.image.views import ImageListCreateAPIView, ImageRetrieveUpdateDestroyAPIView
from apps.gallery.api.client.image.views import ImageListAPIView, ImageRetrieveAPIView
from apps.gallery.api.client.category.views import CategoryImageListAPIView, CategoryImageRetrieveAPIView


urlpatterns = [
    # ------------FOR CLIENTS------------

    # image list and retrieve for clients
    path('client/image/', ImageListAPIView.as_view()),
    path('client/image/<str:pk>/', ImageRetrieveAPIView.as_view()),

    # category list and retrieve for clients
    path('client/category/', CategoryImageListAPIView.as_view()),
    path('client/category/<str:pk>/', CategoryImageRetrieveAPIView.as_view()),

    # ------------FOR ADMIN------------

    # content of images list and retrieve for admin
    path('admin/content-image/', ContentImageListCreateAPIView.as_view()),
    path('admin/content-image/<str:pk>/', ContentImageRetrieveUpdateDestroyAPIView.as_view()),

    # content of category list and retrieve for admin
    path('admin/content-category/', ContentCategoryImageListCreateAPIView.as_view()),
    path('admin/content-category/<str:pk>/', ContentCategoryImageRetrieveUpdateDestroyAPIView.as_view()),

    # image list and retrieve for admin
    path('admin/image/', ImageListCreateAPIView.as_view()),
    path('admin/image/<str:pk>/', ImageRetrieveUpdateDestroyAPIView.as_view()),

    # category list adn retrieve for admin
    path('admin/category/', CategoryImageListCreateAPIView.as_view()),
    path('admin/category/<str:pk>/', CategoryImageRetrieveUpdateDestroyAPIView.as_view()),
]
