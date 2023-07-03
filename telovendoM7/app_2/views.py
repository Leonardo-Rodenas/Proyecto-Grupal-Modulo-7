from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from app_1.models import Cliente,Pedido,DetallePedido,Producto
from django.contrib.auth import get_user_model


def registrar_usuario(request):
    if request.method == 'POST':
        # Obtain the form data
        rut = request.POST['rut']
        first_name = request.POST['first_name']
        segundo_nombre = request.POST['segundo_nombre']
        last_name = request.POST['last_name']
        segundo_apellido = request.POST['segundo_apellido']
        username = request.POST['username']
        telefono = request.POST['telefono']
        email = request.POST['email']
        direccion = request.POST['direccion']
        password = get_random_string(length=6)


        # Check if the user already exists
        if Cliente.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya está en uso.'})

        # Check if the email already exists
        if Cliente.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El email ya está en uso.'})

        # Create the new user
        Cliente.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name, 
            rut=rut, segundo_nombre=segundo_nombre, segundo_apellido=segundo_apellido, telefono=telefono,
            direccion=direccion
        )

        # Send the email
        send_mail(
            'Somos de TeLoVendo, traemos tu contraseña ♥️',
            'Hola ' + first_name + ' ' + last_name + ', tu contraseña es: ' + password,
            'talento@fabricadecodigo.dev',
            [email],
            fail_silently=False
        )

        # Redirect to a success page or any desired page
        return redirect('telovendo')

    # If it's a GET request, display the registration form
    return render(request, 'registro.html')

def registrar_pedido(request):
    if request.method == 'POST':
        id = request.POST['cliente']
        direccion = request.POST['direccion']
        cliente = Cliente.objects.get(id=id)
        metodo = request.POST['metodo']
        medio = request.POST['medio']
        pedido=Pedido(metodo_pago=metodo,mediopedido=medio,idcliente=cliente)
        pedido.save()
        cliente.direccion = direccion
        cliente.save()
        return redirect('detalle_pedido', pedido.id )

def edicionProducto(request):
    if request.method == 'POST':
        id = request.POST['id']
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock= request.POST['stock']
        productoedit=Producto.objects.get(id=id)
        productoedit.nombre=nombre
        productoedit.precio_venta=precio
        productoedit.stock=stock
        productoedit.save()
        return redirect('gestion_producto')
    return redirect('gestion_producto')


def CreacionDetalle(request,id):
    useractual=request.user
    if request.method == 'POST':
        idproducto = request.POST['producto']
        pedido = Pedido.objects.get(id=id)
        producto = Producto.objects.get(id=idproducto)
        cantidad = request.POST['cantidad']
        precio=int(cantidad)*int(producto.precio_venta)
        newdetalle=DetallePedido(idpedido=pedido,idproducto=producto,cantidad=cantidad,precio=precio)
        newdetalle.save()
        producto.stock=producto.stock-int(cantidad)
        producto.save()
        pedido.precio_total=precio+pedido.precio_total
        if useractual.is_staff:
            pedido.pedido_staff=True   
        pedido.save()
    return redirect('detalle_pedido',id)

#class ListaTareas(LoginRequiredMixin, ListView):
   # model = Tarea # Modelo a utilizar
    #context_object_name = 'Tareas'  # Le da un nuevo nombre en el for para que no se llame simplemente object
    #template_name = 'templates_app/app_1/lista_tareas.html' # modifica la ruta el template para que no sea necesario que se llame tarea_detail.html (prefijo = modelo, sufijo=list, así lo busca por defecto al usar estas clases heredadas)
    #ordering = ['fecha_vencimiento'] # Ordena por fecha vencimiento

    #def get_queryset(self): # Acá ordeno las querys para ordenar las tareas 
    #    queryset = super().get_queryset()
     
    #   queryset = queryset.filter(usuario=self.request.user)
     #   return queryset

    #def get_context_data(self, **kwargs): # Recibe las tareas sólo del usuario logueado y no todas las tareas en la base de datos.
     #   context = super().get_context_data(**kwargs)
      #  tareas_usuario = self.get_queryset()
       # context['Tareas'] = tareas_usuario
        #context['count'] = tareas_usuario.filter(estado='Pendiente').count()
        #return context

# def registrar_pedido(request):
#     actualuser = request.user
#     productos = Producto.objects.all()
#     precio=0
#     if request.method == 'POST':
#         metodo = request.POST['metodo']
#         direccion= request.POST['direccion']
#         produc = request.POST['produc']
#         cantidad = request.POST['cantidad']
        
#         for prduct in productos:
#             if str(prduct.id)==produc:
#                 precio=int(cantidad)*prduct.precio_venta
#                 break
#         actualuser.direccion=direccion
#         actualuser.save()
#         newpedido=Pedido(idcliente=actualuser,metodo_pago=metodo,precio_total=precio)
#         newdetalle=DetallePedido(idproducto=prduct,cantidad=cantidad,precio=precio,idpedido=newpedido)
#         newpedido.save()
#         newdetalle.save()
        
#         return redirect('lista_pedido')