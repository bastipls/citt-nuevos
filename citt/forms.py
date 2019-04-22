from django import forms
from .models import Alumno,Evento

class AlumnoForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut_alumno'].widget.attrs.update({'required':'True'})



    class Meta:
        model = Alumno
        fields = ('rut_alumno',)
class EventoForm (forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre_evento'].widget.attrs.update({'required':'True'})

    class Meta:
        model = Evento
        fields = ('nombre_evento',)