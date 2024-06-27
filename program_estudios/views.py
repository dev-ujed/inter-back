from rest_framework import viewsets
from .serializers import CarreraSerializer, EscuelasMovSerializer, CarrerasInterSerializer
from .models import EscuelasMov, Carreras, CarrerasInter

class EscuelasMovViewSet(viewsets.ModelViewSet):
    queryset = EscuelasMov.objects.all()
    serializer_class = EscuelasMovSerializer

class CarrerasViewSet(viewsets.ModelViewSet):
    queryset = Carreras.objects.all()
    serializer_class = CarreraSerializer

class CarrerasInterViewSet(viewsets.ModelViewSet):
    queryset = CarrerasInter.objects.all()
    serializer_class = CarrerasInterSerializer

