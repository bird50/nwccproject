from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet
from .models import Rs_Cat
from .serializers import Rs_CatSerializer

def index(request):
    return render(request, 'rs_cat/home.html')
# Create your views here.

def list(request):
    rs_cat_list = Rs_Cat.objects.all()
    paginator = Paginator(rs_cat_list, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'rs_cat/list.html', {'page_obj': page_obj})


class rs_catViewSet(ModelViewSet):
    queryset = Rs_Cat.objects.all()
    serializer_class = Rs_CatSerializer
    
'''    
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='nwcc API')
'''
