from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Rs_Cat

def index(request):
    return render(request, 'rs_cat/home.html')
# Create your views here.

def list(request):
    rs_cat_list = Rs_Cat.objects.all()
    paginator = Paginator(rs_cat_list, 50) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'rs_cat/list.html', {'page_obj': page_obj})