from django.db import models


# Create your models here.
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key = True)
    rut_alumno = models.CharField(max_length = 10) 

def __str__(self):
    
    return self.rut_alumno 
