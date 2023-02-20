from django.db import models
from .validators import validar_par
from .validators import nombre_no_permitido
from .validators import formapago_no_permitido
from .validators import validar_precio_garantia
from .validators import validar_monto_deuda

class FormaPago(models.Model):
    nombre = models.CharField(max_length=255, validators=[formapago_no_permitido])
    def __str__(self):
        return self.nombre
    
class Cliente(models.Model):
    ci = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255, validators=[nombre_no_permitido])
    fechanac = models.DateTimeField()
    actividad = models.CharField(max_length=255)
    def __str__(self):
        return self.nombre

class Garantia(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_precio_garantia])
    def __str__(self):
        return self.nombre

class Moneda(models.TextChoices):
    Bs = 'Bs.', 'Bolivianos',
    Sus = '$us', 'Dolares'

class Deuda(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_monto_deuda])
    moneda = models.CharField(
        max_length= 3,
        choices= Moneda.choices,
        default= Moneda.Bs
    )
    nro_cuotas = models.IntegerField()
    tasa = models.DecimalField(decimal_places=2, max_digits=10)
    
    formapago = models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    Garantia = models.ForeignKey(Garantia, on_delete=models.CASCADE)
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return (self.fecha, self.Cliente, self.monto, self.moneda)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

