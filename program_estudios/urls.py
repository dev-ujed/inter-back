from django.urls import path
from .views import listaCarreras, movDestinos

urlpatterns = [
    path('carreras/', listaCarreras.as_view(), name='lista_carreras'),
    path('mov-carreras/', movDestinos.as_view(), name='movDestinos'),
]

#Filtrar por carrera: /mov-carreras/?carrera_id=1
# por disponibilidad: /mov-carreras/?disponible=true
#ambos: /mov-carreras/?carrera_id=1&disponible=true