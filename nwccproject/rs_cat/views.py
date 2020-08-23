from django.shortcuts import render
from django.core.paginator import Paginator
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .models import Rs_Cat
from .serializers import Rs_CatSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.core import serializers

def index(request):
    return render(request, 'rs_cat/index.html')
# Create your views here.

def list(request):
    if request.GET.get('search'):
        search=request.GET.get('search')
        q1= Rs_Cat.objects.filter(keyword__contains=search)
        q2= Rs_Cat.objects.filter(description__contains=search)
        q3= Rs_Cat.objects.filter(name__contains=search)
        rs_cat_list=q1.union(q2,q3)    
    else:
        rs_cat_list = Rs_Cat.objects.all()


    myjson = serializers.serialize("json",rs_cat_list)
    paginator = Paginator(rs_cat_list, 20) 
    page_number = request.GET.get('page')
    search = request.GET.get('search')
    page_obj = paginator.get_page(page_number)
    print("search:", search)
    #print(myjson)
    return render(request, 'rs_cat/list.html', {'page_obj': page_obj})


def detail(request,id):
    print("id=",id)
    det=Rs_Cat.objects.get(id=id)
    meta_fields=dict()
    for a in Rs_Cat._meta.get_fields():
        meta_fields.update({a.name:a.verbose_name})
    #print(meta_fields)
    return render(request, 'rs_cat/detail.html', {'content': {'detail':det,'meta_fields':meta_fields}})


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
