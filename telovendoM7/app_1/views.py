from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'index.html')

def PerfilUsuario(request):
    return render(request, 'perfil_usuario.html')

class VistaLoginCustom(LoginView):
    template_name = 'login.html'
    fields = '__all__' # Crea todos los campos para el formulario a partir del modelo predefinido de Django
    redirect_authenticated_user = True # Rediderciona si el login es exitoso
    
    def get_success_url(self):
        return reverse_lazy('perfil_usuario') # Lugar al que se es redirecionado si el login es exitoso
