from django.urls import path
from . import views
from .views import VistaLoginCustom
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.index, name='telovendo'), 
    path('login/', VistaLoginCustom.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('perfil_usuario/', views.PerfilUsuario, name='perfil_usuario'), 
]