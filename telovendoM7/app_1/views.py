from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Pedido
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.http import require_POST

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

class ListaPedidos (ListView):
    model = Pedido
    context_object_name = 'pedidos'
    

class DetallePedido(DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'app_1/detalle_pedido.html'

    # @require_POST
    # def cambiar_estado_pedido(self, request, *args, **kwargs):
    #     pedido = self.get_object()
    #     nuevo_estado = request.POST.get('estado')
    #     pedido.estado = nuevo_estado
    #     pedido.save()
    #     return redirect('detalle_pedido', pk=pedido.pk)

    # def post(self, request, *args, **kwargs):
    #     return self.cambiar_estado_pedido(request, *args, **kwargs)
    
    # def get(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     context = self.get_context_data(object=self.object)
    #     return self.render_to_response(context)
