from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Web Application Endpoint
    path('students/', include('students.urls')),

    # API Endpoint
    path('api/v1/', include('api.urls')),
    
]