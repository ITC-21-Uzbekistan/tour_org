from django.urls import path
from .views import ListCreateLanguageView, RetrieveUpdateDestroyLanguageView

urlpatterns = [
    path('', ListCreateLanguageView.as_view()),
    path('<str:pk>/', RetrieveUpdateDestroyLanguageView.as_view()),
]