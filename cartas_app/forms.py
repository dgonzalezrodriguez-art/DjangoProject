from django import forms
from .models import Carta


class FormularioCarta(forms.ModelForm):
    class Meta:
        # 1. Le decimos a Django en qué modelo se basa este formulario
        model = Carta

        # 2. Le decimos qué campos queremos que el usuario rellene
        fields = ['nombre', 'rareza', 'descripcion', 'enlace_imagen_frontal', 'enlace_imagen_trasera']

        # 3. (Opcional pero recomendado) Le añadimos clases CSS (Bootstrap) para que se vea bonito
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Monkey D. Luffy'}),
            'rareza': forms.Select(attrs={'class': 'form-select'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'enlace_imagen_frontal': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Enlace a la imagen...'}),
            'enlace_imagen_trasera': forms.URLInput(
                attrs={'class': 'form-control', 'placeholder': 'Enlace a la imagen...'}),
        }
