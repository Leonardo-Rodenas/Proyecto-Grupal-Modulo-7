from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView
from .views import ListaPedidos, DetallePedido
from app_2.views import registrar_pedido

urlpatterns = [
    path('', views.index, name='telovendo'), 
    path('login/', VistaLoginCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('lista_pedido/', ListaPedidos.as_view(), name='lista_pedido'), 
    path('detalle_pedido/<int:pk>/', DetallePedido.as_view(), name='detalle_pedido'),
    path('lista_pedido/\\#\\Z',registrar_pedido,name='registrar_pedido'),
    # path('detalle_pedido/<int:pk>/cambiar_estado/', DetallePedido.as_view(), name='detalle_ cambiar_estado'),
]