from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Pedido, DetallePedido
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'index.html')

User = get_user_model()

class FormularioRegistroUsuarioPersonalizado(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class VistaLoginCustom(LoginView):
    template_name = 'login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo predefinido de Django
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    def get_success_url(self):
        return reverse_lazy('lista_pedido') # Lugar al que se es redirecionado si el login es exitoso

class ListaPedidos (LoginRequiredMixin, ListView):
    model = Pedido
    context_object_name = 'pedidos'
    
class DetallePedido(LoginRequiredMixin, DetailView):
    model = DetallePedido
    context_object_name = 'detallepedido'
    template_name = 'app_1/detalle_pedido.html'

    def post(self, request, *args, **kwargs):
        pedido = self.get_object()
        nuevo_estado = request.POST.get('estado')
        pedido.estado = nuevo_estado
        pedido.save()
        pedido.refresh_from_db()  # Actualizar el objeto desde la base de datos
        return redirect('detalle_pedido', pk=pedido.pk)

def gestionProducto(request):
    return render(request,'app_1/gestion_pedido.html')