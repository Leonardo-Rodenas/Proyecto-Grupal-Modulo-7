from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.shortcuts import redirect
from .models import Pedido,DetallePedido,Cliente,Producto
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def index(request):
    return render(request, 'index.html')

user = get_user_model()

class FormularioRegistroUsuarioPersonalizado(UserCreationForm):
    class Meta:
        model = user
        fields = ['username', 'email']

class VistaLoginCustom(LoginView):
    template_name = 'login.html'
    fields = ['username', 'password'] # Crea todos los campos para el formulario a partir del modelo predefinido de Django
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    
    def get_success_url(self):

        return reverse_lazy('lista_pedido') # Lugar al que se es redirecionado si el login es exitoso



# class ListaPedidos (LoginRequiredMixin, ListView):
#     model = DetallePedido
#     context_object_name = 'detallepedidos'
#     template_name = 'app_1/pedido_list.html'

"""' Vimos que acabas de iniciar sesion en nuestra pagina TeLoVendo"""

@login_required
def ListaPedidos(request):
    actualuser = request.user
    send_mail(
            'Telovendo Alerta de inicio de Sesion','Hola'+ actualuser.first_name + actualuser.last_name +' alguien acaba de iniciar sesion en tu cuenta de Te lo Vendo:'+ actualuser.username +', si no has sido tú, por favor revisa tu contraseña y procura cambiarla si es necesario, recuerda no compartirla con nadie.\n\n\n Atte. equipo de Telovendo',
            'talento@fabricadecodigo.dev',
            [actualuser.email],
            fail_silently=False
        ) 
   # pedidos=Pedido.objects.all()
    #detallepedido=[]
    #for pedido in pedidos:
    #    detallepedido.append(pedido.detallepedido_set.all())
     

    return render(request, 'pedido_list.html')
    #,{'detallepedidos':detallepedido}

def CrearDetalle(request,id):
    pedido= Pedido.objects.get(id=id)
    return render(request,"crear_detalle.html",{"pedido":pedido})
   
def editarDetalle():
    pass

def is_staff(Cliente):
    return Cliente.is_staff 

<<<<<<< HEAD
def confirmarPedido(request):
    pass
=======
def confirmarPedido(request,id):
    if request.method == 'POST':
        pedido = Pedido.objects.get(id=id)
        pedido.is_modificable=False   
        pedido.save()
    return redirect('lista_pedido')
>>>>>>> Rafa

@user_passes_test(is_staff)
def gestionProducto(request):
    users = Cliente.objects.all()
    return render(request,'app_1/gestion_producto.html')

def editarProducto(request,id):
    produc=Producto.objects.get(id=id)
    return render(request,"editar_producto.html",{"producto":produc})

class DetallePedido(LoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'app_1/detalle_pedido.html'

    def post(self, request, *args, **kwargs):
        pedido = self.get_object()
        nuevo_estado = request.POST.get('estado')
        pedido.estado = nuevo_estado
        pedido.save()
        pedido.refresh_from_db()  # Actualizar el objeto desde la base de datos
        return redirect('detalle_pedido', pk=pedido.pk)



