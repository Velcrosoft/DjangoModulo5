from rest_framework import serializers
from .models import FormaPago
from .models import Cliente
from .models import Deuda
from .models import Garantia

class FormaPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class DeudaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deuda
        fields = "__all__"

class GarantiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garantia
        fields = "__all__"