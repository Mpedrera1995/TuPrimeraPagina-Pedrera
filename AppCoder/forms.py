from django import forms
from .models import Reseña, Truco, Consola

class ReseñaForm(forms.ModelForm):
    class Meta:
        model = Reseña
        fields = ['videojuego', 'contenido', 'autor']
        labels = {
            'videojuego': 'Nombre del videojuego',
            'contenido': 'Contenido de la reseña',
            'autor': 'Tu nombre',
        }

class TrucoForm(forms.ModelForm):
    class Meta:
        model = Truco
        fields = ['videojuego', 'descripcion']
        labels = {
            'videojuego': 'Nombre del videojuego',
            'descripcion': 'Descripción del truco',
        }

class ConsolaForm(forms.ModelForm):
    class Meta:
        model = Consola
        fields = ['nombre', 'empresa', 'año_lanzamiento']
        labels = {
            'nombre': 'Nombre de la consola',
            'empresa': 'Fabricante',
            'año_lanzamiento': 'Año de lanzamiento',
        }

class BuscarReseñaForm(forms.Form):
    videojuego = forms.CharField(
        label='Buscar reseñas por videojuego',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. God of War'})
    )
