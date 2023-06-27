from app_1.models import Producto


def ListaProductos(request):
    productos = Producto.objects.all()
    return {'productos':productos}