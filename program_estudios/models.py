from django.db import models

#Modelo basado en el excel de los programas de estudios de cada carrera

from django.db import models

# Son las escuelas a las que los estudiantes pueden ir
class EscuelasMov(models.Model):
    nombre = models.CharField(max_length=150)
    pagina_web = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

# Son las carreras que cuenta el plan de estudios
class Carreras(models.Model):
    carrera = models.CharField(max_length=150)

    def __str__(self):
        return self.carrera

# Es la relacion para ver que escuela esta disponible en que carrera y poder hacer el viaje 
class CarrerasInter(models.Model):
    disponible = models.BooleanField(default=False)
    carreras = models.ForeignKey(Carreras, on_delete=models.CASCADE, related_name='carreras_inter')
    escuelas_mov = models.ForeignKey(EscuelasMov, on_delete=models.CASCADE, related_name='carreras_inter')

