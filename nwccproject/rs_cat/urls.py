from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    path('cat/', views.list, name='list'),
    path('detail/<int:id>', views.detail, name='detail'),
]