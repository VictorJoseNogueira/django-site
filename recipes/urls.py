from recipes.views import _home
from django.urls import path


urlpatterns = [
    
    path('', _home),
]