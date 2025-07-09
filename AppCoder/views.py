from django.shortcuts import render, redirect
from .forms import ReseñaForm, TrucoForm, ConsolaForm, BuscarReseñaForm
from .models import Reseña

def inicio(request):
    formulario = BuscarReseñaForm()
    resultados = None

    if request.method == 'POST':
        formulario = BuscarReseñaForm(request.POST)
        if formulario.is_valid():
            juego = formulario.cleaned_data['videojuego']
            resultados = Reseña.objects.filter(videojuego__icontains=juego)

    return render(request, 'AppCoder/inicio.html', {
        'formulario': formulario,
        'resultados': resultados
    })

def crear_reseña(request):
    if request.method == 'POST':
        form = ReseñaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseñas:crear_reseña')
    else:
        form = ReseñaForm()
    return render(request, 'AppCoder/reseñas.html', {'form': form})

def agregar_truco(request):
    if request.method == 'POST':
        form = TrucoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseñas:agregar_truco')
    else:
        form = TrucoForm()
    return render(request, 'AppCoder/truco.html', {'form': form})

def agregar_consola(request):
    if request.method == 'POST':
        form = ConsolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseñas:agregar_consola')
    else:
        form = ConsolaForm()
    return render(request, 'AppCoder/consola.html', {'form': form})
