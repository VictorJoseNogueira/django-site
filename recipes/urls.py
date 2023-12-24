from django.urls import path
from . import views

urlpatterns = [
    
    path('', views._home),
    path('recipes/<int:id>/', views.recipe),

]