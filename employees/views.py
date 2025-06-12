from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Employees API is working!")