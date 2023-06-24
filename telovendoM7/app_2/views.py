from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

def registrar_usuario(request):
    if request.method == 'POST':
        # Obtain the form data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = get_random_string(length=6)


        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'registro.html', {'error': 'El nombre de usuario ya está en uso.'})

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'registro.html', {'error': 'El email ya está en uso.'})

        # Create the new user
        user = User.objects.create_user(
            username=username, password=password, email=email, first_name=first_name, last_name=last_name)

        # Send the email
        send_mail(
            'Hola, tu contraseña ha llegado.',
            'Hola ' + first_name + ' ' + last_name + ', tu contraseña es: ' + password,
            'talento@fabricadecodigo.dev',
            [email],
            fail_silently=False
        )

        # Redirect to a success page or any desired page
        return redirect('telovendo')

    # If it's a GET request, display the registration form
    return render(request, 'registro.html')

