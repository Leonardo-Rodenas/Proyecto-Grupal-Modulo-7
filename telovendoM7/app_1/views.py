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
    #actualuser = request.user
    #send_mail(
    #    'Telovendo Alerta de inicio de Sesion','Hola '+ actualuser.first_name + ' ' + actualuser.last_name +' acabas de iniciar sesion en tu cuenta de Te lo Vendo: '+ actualuser.username +', si no has sido tú, por favor revisa tu contraseña y procura cambiarla si es necesario, recuerda no compartirla con nadie.\n\n\n Atte. equipo de Telovendo',
    #    'talento@fabricadecodigo.dev',
    #    [actualuser.email],
    #    fail_silently=False
    #    ) 
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

def confirmarPedido(request,id):
    if request.method == 'POST':
        pedido = Pedido.objects.get(id=id)
        pedido.is_modificable=False   
        pedido.save()
    return redirect('lista_pedido')

@user_passes_test(is_staff)
def gestionProducto(request):
    users = Cliente.objects.all()
    return render(request,'app_1/gestion_producto.html')

def editarProducto(request,id):
    produc=Producto.objects.get(id=id)
    return render(request,"editar_producto.html",{"producto":produc})

from django.core.mail import send_mail
from django.shortcuts import redirect

class DetallePedido(LoginRequiredMixin, DetailView):
    model = Pedido
    context_object_name = 'pedido'
    template_name = 'app_1/detalle_pedido.html'
    
    def post(self, request, *args, **kwargs):
        pedido = self.get_object()
        nuevo_estado = request.POST.get('estado')
        pedido.estado = nuevo_estado
        pedido.save()
        nombre = str(pedido.idcliente.first_name)
        apellido = str(pedido.idcliente.last_name)
        num = str(pedido.id)
        
        if nuevo_estado == 'Pendiente':
            return redirect('detalle_pedido', pk=pedido.pk)
        elif nuevo_estado == 'En Despacho':
            cabeza = '🔔 Información del estado de tu pedido N° ' + num + ': En Despacho 🥵🥵😱😰'
            cuerpo = 'Hola 🖐️ '+ nombre + ' ' + apellido +' te informamos que el estado de tu pedido ha cambiado a: "En depacho", Gracias por comprar en Te Lo Vendo. \n\n\n Atte. equipo de Telovendo'
        elif nuevo_estado == 'Entregado':
            cabeza = '🔔 Información del estado de tu pedido N° ' + num + ': Entregado'
            cuerpo = 'Hola 🖐️ '+ nombre + ' ' + apellido + ' agradecemos tu preferencia y estamos felices de anunciarte que tu pedido se encuentra "Entregado". Por favor, revisa el estado de tus productos y avísanos ante cualquier percance. Recuerda que tienes 5 días hábiles post-entregado el producto para realizar cambios sin costo. Estamos atentos a tus comentarios. \n\n\nMuchas gracias. \n\n\n Atte. Equipo de Telovendo'
        elif nuevo_estado == 'En Preparación':
            cabeza = '🔔 Información del estado de tu pedido N° ' + num + ': En Preparación'
            cuerpo = 'Confirmamos tu pedido \n\n Hola 🖐️ '+ nombre + ' ' + apellido +'\n\nAgradecemos tu preferencia. Tu pedido '+ num +' se encuentra: ' +  pedido.estado  +'. Te avisaremos cuando se envíe \n\n\n Atte. equipo de TeLoVendo'
        
        pedido.refresh_from_db()  # Actualizar el objeto desde la base de datos
        
        # Send the email
        send_mail(
            cabeza,
            cuerpo,
            'talento@fabricadecodigo.dev',
            [pedido.idcliente.email],
            fail_silently=False
        )
        
        return redirect('detalle_pedido', pk=pedido.pk)



