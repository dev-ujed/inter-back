from django.urls import path, include
from rest_framework import routers
from program_estudios import views 
#urlpatterns = [
    #path('carreras/', listaCarreras.as_view(), name='lista_carreras'),
    #path('mov-carreras/', movDestinos.as_view(), name='movDestinos'),
#]

router=routers.DefaultRouter()
router.register(r'carreras', views.CarrerasViewSet)
router.register(r'mov-carreras', views.EscuelasMovViewSet)
router.register(r'carreras-inter', views.CarrerasInterViewSet)

urlpatterns = [
    path('', include(router.urls))
]


from django.urls import path
from .views import *

urlpatterns = [
    path('carreras/', listaCarreras.as_view(), name='lista_carreras'),
    path('mov-carreras/', movDestinos.as_view(), name='movDestinos'),
]

#Filtrar por carrera: /mov-carreras/?carrera_id=1
# por disponibilidad: /mov-carreras/?disponible=true
#ambos: /mov-carreras/?carrera_id=1&disponible=true