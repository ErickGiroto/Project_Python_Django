from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html') # Redenizar o arquivo HTML com o 'render'

def sobre(request):
    return HttpResponse('SOBRE 2')

def contato(request):
    return HttpResponse('CONTATO 2')