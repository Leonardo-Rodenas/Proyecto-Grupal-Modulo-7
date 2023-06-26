from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView
from .views import ListaPedidos

urlpatterns = [
    path('', views.index, name='telovendo'), 
    path('login/', VistaLoginCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('lista_pedido/', ListaPedidos.as_view(), name='lista_pedido'), 
]