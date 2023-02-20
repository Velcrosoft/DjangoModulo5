from django.contrib import admin
from .models import FormaPago
from .models import Cliente
from .models import Garantia
from .models import Deuda


# Register your models here.

admin.site.register(FormaPago)
admin.site.register(Cliente)
admin.site.register(Garantia)
admin.site.register(Deuda)
