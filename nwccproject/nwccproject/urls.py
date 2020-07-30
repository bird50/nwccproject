"""nwccproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view
from rs_cat.views import rs_catViewSet
'''
กรณีใช้ Router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('rs_cat', rs_catViewSet)
'''

schema_view = get_swagger_view(title='NWCC API')

rs_cat_list = rs_catViewSet.as_view({
    'get': 'list'
})
rs_cat_detail = rs_catViewSet.as_view({
    'get': 'retrieve'
})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nwcc.urls')),
    path('nwcc/', include('nwcc.urls')),
    path('rs_cat/', include('rs_cat.urls')),
    #path('api/',include(router.urls)), # กรณีใช้ Router
    path('api_doc/',schema_view,name="api_doc"),
    path('api_v1/rs_cat/',rs_cat_list),
    path('api_v1/rs_cat/<int:pk>',rs_cat_detail),
]





if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)