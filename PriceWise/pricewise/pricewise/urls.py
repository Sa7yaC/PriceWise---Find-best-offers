from django.contrib import admin
from django.urls import path
from . import extract

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',extract.index,name ='index'),
    path('getLink', extract.getLink, name='getLink')
]
