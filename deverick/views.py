from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'page/home.html') # Redenizar o arquivo HTML com o 'render'

def sobre(request):
    return render(request, 'page/sobre.html')

def contato(request):
    return render(request, 'page/contato.html')