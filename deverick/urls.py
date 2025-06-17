# Arquivo criado para gerencias as páginas Urls

from django.urls import path
from deverick.views import home

# Cliente(Pede) < (Server)Responde
# Http Request < Http Response

urlpatterns = [
    path('', home),
 

]