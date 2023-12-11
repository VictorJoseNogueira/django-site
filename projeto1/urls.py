from django.contrib import admin
from django.urls import path
from django.http import HttpResponse




#HTTP request
def my_view(request):
    #return HTTP Response 
    #cliente request <- servidor response
    return HttpResponse('uma linda string')


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('rota, e funçao')
    path('sobre/', my_view),
]
