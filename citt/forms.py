from django import forms
from .models import Alumno

class AlumnoForm (forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rut_alumno'].widget.attrs.update({'required':'True'})



    class Meta:
        model = Alumno

        fields = ('rut_alumno',)