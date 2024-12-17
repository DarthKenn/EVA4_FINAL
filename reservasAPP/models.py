from django.db import models
from django.core.exceptions import ValidationError

def validar_cantidad_personas(value):
    if value < 1 or value > 15:
        raise ValidationError("La cantidad de personas debe estar entre 1 y 15.")

class Reserva(models.Model):
    ESTADOS = [
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO_ASISTEN', 'No Asisten'),
    ]

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha = models.DateField()
    hora = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(validators=[validar_cantidad_personas])
    estado = models.CharField(max_length=15, choices=ESTADOS, default='RESERVADO')
    observacion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"
    
def validar_cantidad_personas(value):
    if value < 1 or value > 15:
        raise ValidationError("La cantidad de personas debe estar entre 1 y 15.")