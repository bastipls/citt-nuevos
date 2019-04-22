from django.db import models


# Create your models here.
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key = True)
    rut_alumno = models.CharField(max_length = 10)
    evento_asistio_alumno = models.CharField(max_length = 40, blank=True,null=True)

    def __str__(self):
        
        return self.rut_alumno 
class Evento (models.Model):
    id_evento = models.AutoField(primary_key = True)
    nombre_evento = models.CharField(max_length = 40)
    def __str__(self):

        return self.nombre_evento