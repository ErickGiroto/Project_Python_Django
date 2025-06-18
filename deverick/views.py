from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'page/pages/home.html', context= { 
        'name' : 'Erick Giroto',
        })

# Redenizar o arquivo HTML com o 'render' e Define uma Variavel 'name'