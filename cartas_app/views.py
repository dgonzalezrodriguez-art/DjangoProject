
from django.shortcuts import render, redirect, get_object_or_404
from .models import Carta
from .forms import FormularioCarta

# 1. Página de inicio (Home)
def home(request):
    return render(request, 'cartas.html')

# 2. Página para ver todas las cartas
def ver_cartas(request):
    cartas = Carta.objects.all()  # Traemos todas las cartas de la base de datos
    return render(request, 'ver_cartas.html', {'cartas': cartas})

# 3. Página para crear una carta
def crear_carta(request):
    if request.method == 'POST':
        form = FormularioCarta(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_cartas') # Al terminar, nos manda a la lista
    else:
        form = FormularioCarta()
    return render(request, 'crear_carta.html', {'form': form})

# 4. Función para borrar carta
def borrar_carta(request, pk):
    carta = get_object_or_404(Carta, pk=pk)
    carta.delete()
    return redirect('ver_cartas')

# 5. Página para modificar carta
def modificar_carta(request, pk):
    carta = get_object_or_404(Carta, pk=pk)
    if request.method == 'POST':
        form = FormularioCarta(request.POST, instance=carta)
        if form.is_valid():
            form.save()
            return redirect('ver_cartas')
    else:
        form = FormularioCarta(instance=carta)
    return render(request, 'crear_carta.html', {'form': form, 'editando': True})
