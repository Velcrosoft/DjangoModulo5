from django.core.exceptions import ValidationError

def validar_par(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value) no es un numero par',
            params={'value': value}
        )
    
def nombre_no_permitido(value):
    if value == 'Marcelo':
        raise ValidationError(
            'Ese es el nombre del docente y no se permite',
            params={'value': value}
        )

def formapago_no_permitido(value):
    if value == 'Diario':
        raise ValidationError(
            'No se permite esa forma de pago',
            params={'value': value}
        )

def validar_precio_garantia(value):
    if value < 10000: #no se aceptar garantias con valor menor a 10000
        raise ValidationError(
            'Debe dejar una garantia con valor mayor a 10000',
            params={'value': value}
        )

def validar_monto_deuda(value):
    if value > 50000: #no se da credito mayor a 50000
        raise ValidationError(
            'No se puede dar credito mayor a 50000',
            params={'value': value}
        )
