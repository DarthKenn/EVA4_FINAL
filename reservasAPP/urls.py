from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('reservas/', lista_reservas, name='lista-reservas'),
    path('reservas/crear/', crear_reserva, name='crear-reserva'),
    path('reservas/editar/<int:pk>/', editar_reserva, name='editar-reserva'),
    path('reservas/eliminar/<int:pk>/', eliminar_reserva, name='eliminar-reserva'),
    path('reservas/', lista_reservas, name='lista-reservas'),
    path('api/reservas/', ReservaListCreateView.as_view(), name='reservas-list-create'),
    path('api/reservas/<int:pk>/', ReservaRetrieveUpdateDeleteView.as_view(), name='reserva-detail'),
]
