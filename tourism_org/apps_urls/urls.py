from django.urls import path, include

urlpatterns = [
    path('language/', include('apps.language.urls')),
    path('gallery/', include('apps.gallery.urls')),
    path('countries/', include('apps.country.urls')),
    # path('regions/', include('apps.region.urls')),
]
