from django.contrib import admin
from .models import Cliente, Direccion, Clasificacion, Producto, DetallePedido, Pedido

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Direccion)
admin.site.register(Clasificacion)
admin.site.register(Producto)
admin.site.register(DetallePedido)
admin.site.register(Pedido)
# admin.site.register(Direccion)

