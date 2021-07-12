from django import forms
from applications.persona.models import Empleado

class EmpleadoForm(forms.ModelForm):
    
    class Meta:
        model = Empleado
        fields = (
            "first_name",
            "last_name",
            "job",
            "departamento",
            "habilidades",
            'avatar'
        )
        widgets = {
            'first_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese nombres'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'placeholder':'Ingrese apellidos'
                }
            ),
            'habilidades': forms.CheckboxSelectMultiple()

        }

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"]
        if len(first_name) < 2:
            raise forms.ValidationError("Error nombre")
        return first_name