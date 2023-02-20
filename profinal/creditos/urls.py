from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"apiformapagos", views.FormaPagoViewSet)
router.register(r"apiclientes", views.ClienteViewSet)
router.register(r"apideudas", views.DeudaViewSet)

urlpatterns = [
    path('contact/<str:name>', views.contact, name="contact"),
    #path('', views.index, name='index'),
    path('formapagos',views.formapago, name='formapagos'),
    path('clientes',views.ClienteFormView, name='clientes'),
    path('garantia/crear', views.GarantiaCreateView.as_view()),
    path('deuda/contador', views.deudas_count, name='contador'),
    path('', include(router.urls)),

]
