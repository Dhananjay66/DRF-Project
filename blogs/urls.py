from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),  # or your actual API view
]