from recipes.views import _home,_sobre,_contato
from django.urls import path


urlpatterns = [
    
    path('', _home),
    path('sobre/', _sobre),
    path('contato/', _contato),
    #path('rota, e funçao')
   
]