from django.urls import path
from .views import ListCreateLanguageView, RetrieveUpdateDestroyLanguageView

urlpatterns = [
    path('', ListCreateLanguageView.as_view()),
    path('<int:pk>/', RetrieveUpdateDestroyLanguageView.as_view()),
]