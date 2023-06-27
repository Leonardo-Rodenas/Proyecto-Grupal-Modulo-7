from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Cliente
from .models import Pedido
from django.http import HttpResponse
from django import template
from django.template import Context
from django.views.generic.detail import DetailView
from .models import Pedido

# Create your views here.
def index(request):
    return render(request, 'index.html')

# def PerfilUsuario(request):
#     return render(request, 'perfil_usuario.html')

class VistaLoginCustom(LoginView):
    template_name = 'login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo predefinido de Django
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    def get_success_url(self):
        return reverse_lazy('lista_pedido') # Lugar al que se es redirecionado si el login es exitoso

class ListaPedidos (ListView):
    model = Pedido
    context_object_name = 'pedidos'
    

class DetallePedido(DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'app_1/detalle_pedido.html'
