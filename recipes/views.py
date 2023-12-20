from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.



def _home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Victor Nogueira',
    })
