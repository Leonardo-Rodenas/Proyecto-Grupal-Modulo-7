from app_1.models import Producto,Cliente,Pedido,DetallePedido


def ListaProductos(request):
    productos = Producto.objects.all()
    return {'productos':productos}

def ListaClientes(request):
    clientes = Cliente.objects.all()
    return{'clientes':clientes}

def ListaPedidos(request):
    pedido = Pedido.objects.all()
    return{'pedidos': pedido}

def ListaDetallesPedido(request):
    detallepedido = DetallePedido.objects.all()
    return{'detallepedidos':detallepedido}