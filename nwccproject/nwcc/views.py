from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("Hello, This is NWCC App")

def index(request):
    return render(request, 'index.html')
# Create your views here.