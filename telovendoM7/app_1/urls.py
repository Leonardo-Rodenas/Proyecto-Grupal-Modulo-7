from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView
from .views import ListaPedidos, DetallePedido,gestionProducto,editarProducto,CrearDetalle,editarDetalle,confirmarPedido,cancelarPedido
from app_2.views import registrar_pedido,edicionProducto,CreacionDetalle

urlpatterns = [
    path('', views.index, name='telovendo'), 
    path('login/', VistaLoginCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('lista_pedido/', ListaPedidos, name='lista_pedido'), 
    path('detalle_pedido/<int:pk>/', DetallePedido.as_view(), name='detalle_pedido'),
    path('detalle_pedido/crear_detalle/<id>', CrearDetalle, name='crear_detalle'),
    path('detalle_pedido/<id>', CreacionDetalle, name='creacion_detalle'),
    path('editarDetalle/<id>', editarDetalle, name='editar_detalle'),
    path('lista_pedido/\\#\\Z',registrar_pedido,name='registrar_pedido'),
    path('gestion_producto/', gestionProducto, name='gestion_producto'),
    path('gestion_producto/<id>',editarProducto, name="edita_producto"),
    path('edicion_producto',edicionProducto,name="edicion_producto"),
    path('actpedido/<id>',confirmarPedido,name="confirmarpedido"),
    path('cancelarpedido/<id>',cancelarPedido,name="cancelar_pedido"),
    path('detalle_pedido/<int:pk>/cambiar_estado/', DetallePedido.as_view(), name='detalle_ cambiar_estado'),
]