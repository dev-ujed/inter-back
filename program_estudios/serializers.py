from rest_framework import serializers
from .models import Carreras, CarrerasInter, EscuelasMov

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = ['id', 'carrera']

class EscuelasMovSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscuelasMov
        fields = ['id', 'nombre', 'pagina_web']

class CarrerasInterSerializer(serializers.ModelSerializer):
    carreras = serializers.PrimaryKeyRelatedField(queryset=Carreras.objects.all())
    escuelas_mov = serializers.PrimaryKeyRelatedField(queryset=EscuelasMov.objects.all())

    class Meta:
        model = CarrerasInter
        fields = ['id', 'disponible', 'carreras', 'escuelas_mov']
