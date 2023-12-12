from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.



def _home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Victor Nogueira',
    })


def _contato(request):
    return HttpResponse('contato')


def _sobre(request):
    return HttpResponse('sobre')



