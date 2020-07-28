from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import Rs_Cat
from .serializers import Rs_CatSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

def index(request):
    return render(request, 'rs_cat/index.html')
# Create your views here.

def list(request):
    rs_cat_list = Rs_Cat.objects.all()
    paginator = Paginator(rs_cat_list, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'rs_cat/list.html', {'page_obj': page_obj})





class rs_catViewSet(ReadOnlyModelViewSet):
    queryset = Rs_Cat.objects.all()
    serializer_class = Rs_CatSerializer
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    filterset_fields = ['agency','agency_provided_data', 'status','type_of_data']
    search_fields = ['name', 'keyword','note']
    
    
    
'''    
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='nwcc API')
'''
