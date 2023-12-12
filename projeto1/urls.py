from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.urls import include, path




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')),
    #path('rota, e funçao')
   
] 
