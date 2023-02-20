from django.shortcuts import render
from django.http import HttpResponse
#importamos el modelo
from .models import FormaPago
from .models import Cliente
from .models import Deuda
from .models import Garantia

from .forms import ClienteForm
#definir get_object_404
from django.shortcuts import get_object_or_404

def index(request):
    return HttpResponse('hola desde Django')

#ejemplo contact
def contact(request, name):
    return HttpResponse(f"Bienvenido {name} a la clase de Django")

#templates para los modelos, retornamos un html
#def formapago(request):
#    return render(request, 'formapago.html')
def formapago(request):
    post_nombre = request.POST.get('nombre')
    if post_nombre: #si post_nombre tiene algun valor, ingresa al if
        q = FormaPago(nombre=post_nombre)
        q.save()
    filtro_nombre = request.GET.get('nombre')
    if filtro_nombre:
        fpago = FormaPago.objects.filter(nombre__contains=filtro_nombre)
    else:
        fpago = FormaPago.objects.all()

    return render(request, 'formFormapago.html', {
        "formapagos":fpago
    })

def ClienteFormView(request):
    #si queremos hacer update
    form = ClienteForm()
    cliente = None
    id_cliente = request.GET.get('id')
    if id_cliente:
        cliente = get_object_or_404(Cliente, id=id_cliente)
        print(F"cliente nro: {cliente}")
    if request.method == "POST":
        if cliente:
            form = ClienteForm(request.POST, isinstance = cliente)
        else:
            form = ClienteForm(request.POST)

    if form.is_valid():
        form.save()
    return render(request, "formCliente.html", {'form': form})

#endpoints con modelviewset
#import para api rest
from rest_framework import viewsets
from .serializers import FormaPagoSerializer
from .serializers import ClienteSerializer
from .serializers import DeudaSerializer

class FormaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class DeudaViewSet(viewsets.ModelViewSet):
    queryset = Deuda.objects.all()
    serializer_class = DeudaSerializer

#usando genericApiView
from rest_framework import generics
from .serializers import GarantiaSerializer
class GarantiaCreateView(generics.CreateAPIView, generics.ListAPIView):
    queryset = Garantia.objects.all()
    serializer_class = GarantiaSerializer

#usando api personalizada
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(["GET"])
def deudas_count(request):
    try:
        cantidad = Deuda.objects.count()
        return JsonResponse(
            {
                "cantidad": cantidad
            },
        safe=False,
        status=200,
        )
    except Exception as e:
        return JsonResponse({"Message": str(e)}, status=400)