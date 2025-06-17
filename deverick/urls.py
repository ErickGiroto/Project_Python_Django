# Arquivo criado para gerencias as páginas Urls

from django.urls import path
from deverick.views import home, sobre, contato

# Cliente(Pede) < (Server)Responde
# Http Request < Http Response


# ----- Configuração dentro da urls projeto_python
# dominio.com/erick/sobre
# dominio.com/erick/contato

urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato),

]