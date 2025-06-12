from django.http import HttpResponse

def home(request):
    return HttpResponse("✅ Blogs API is working!")