from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

#from django.core.mail import send_mail
#send_mail('picopalqlee', 'correo de prueba', 'talento@fabricadecodigo.dev',['calderonhernandez.nicolas@gmail.com'], fail_silently=False)
