<<<<<<< HEAD
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

=======
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Carreras, CarrerasInter
from .serializers import CarreraSerializer, CarrerasInterSerializer
from rest_framework import generics

from django.shortcuts import render

class listaCarreras(generics.ListAPIView):
    queryset = Carreras.objects.all()
    serializer_class = CarreraSerializer

class movDestinos(generics.ListAPIView):
    serializer_class = CarrerasInterSerializer

    def get_queryset(self):
        queryset = CarrerasInter.objects.all()
        carrera_id = self.request.query_params.get('carrera_id', None)
        disponible = self.request.query_params.get('disponible', None)

        if carrera_id is not None:
            queryset = queryset.filter(carreras_id=carrera_id)
        
        if disponible is not None:
            disponible = disponible.lower() == 'true'
            queryset = queryset.filter(disponible=disponible)

        return queryset
>>>>>>> e61e18e (Primer commit)
