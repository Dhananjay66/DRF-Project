# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Web Application Endpoint
#     path('students/', include('students.urls')),

#     # API Endpoint
#     path('api/v1/', include('api.urls')),
    
# ]


from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.documentation import include_docs_urls

def home(request):
    html = """
    <h1>🚀 Welcome to the Django REST API</h1>
    <ul>
        <li><a href="/admin/">Admin Panel</a></li>
        <li><a href="/api/">API</a></li>
        <li><a href="/api/students/">Students API</a></li>
        <li><a href="/api/employees/">Employees API</a></li>
        <li><a href="/api/blogs/">Blogs API</a></li>
    </ul>
    """
    return HttpResponse(html)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]