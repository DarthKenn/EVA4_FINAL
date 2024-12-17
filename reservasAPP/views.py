
from rest_framework import generics
from .serializers import ReservaSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Reserva
from .forms import ReservaForm



class ReservaListCreateView(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('fecha')
    serializer_class = ReservaSerializer

class ReservaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

def index(request):
    return render(request, 'index.html')

def lista_reservas(request):
    query = request.GET.get('q', '')
    reservas = Reserva.objects.all().order_by('fecha')
    if query:
        reservas = reservas.filter(nombre__icontains=query) 
    return render(request, 'lista_reservas.html', {'reservas': reservas, 'query': query})

def crear_reserva(request):
    if request.method == 'POST':
        print("Datos recibidos en POST:", request.POST)
        form = ReservaForm(request.POST)
        if form.is_valid():
            print("Formulario válido. Guardando reserva...")
            form.save()
            messages.success(request, 'Reserva creada exitosamente.')
        else:
            print("Errores del formulario:", form.errors)
            messages.error(request, 'Ocurrió un error al crear la reserva.')
    return redirect('lista-reservas')


def editar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Reserva actualizada exitosamente.')
            return redirect('lista-reservas')
        else:
            messages.error(request, 'Ocurrió un error al actualizar la reserva. Verifica los datos ingresados.')
    return redirect('lista-reservas')

def eliminar_reserva(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.delete()
        return redirect('lista-reservas')
    return render(request, 'confirmar_eliminacion.html', {'reserva': reserva})
