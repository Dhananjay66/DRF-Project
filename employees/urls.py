from django.urls import path
from . import views

urlpatterns = [
    # Example: path('', views.EmployeeList.as_view()),
    path('', views.home),  # If you just want a test route
]