from django.contrib import admin
from django.urls import path, include # Incluindo as urls dos Apps

# Cliente(Pede) < (Server)Responde
# Http Request < Http Response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('deverick.urls') ), # Buscando as urls dentro do Apps 'DevErick'
]
