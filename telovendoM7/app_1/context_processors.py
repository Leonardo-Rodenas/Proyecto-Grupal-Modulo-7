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
    pedidos= Pedido.objects.all()
    dp=[]
    for pedido in pedidos:
        detallepedidos=pedido.detallepedido_set.all()
        for detallepedido in detallepedidos:
            dp.append(detallepedido)
    return{'detallepedidos':dp}