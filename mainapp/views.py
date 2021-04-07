from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from mainapp.forms import RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request, 'mainapp/index.html',{
        'title': 'Inicio'
    })

def about(request):

    return render(request, 'mainapp/about.html',{
        'title': 'Sobre nosotros'
    })


def register_pager(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:

        register_form = RegistroForm()

        if request.method == 'POST':
            register_form = RegistroForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Registrado Correctamente')

                return redirect('inicio')


        return render(request, 'users/registro.html',{
            'title': 'Registro de Usuarios',
            'register_form': register_form
        })

def login_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')
    else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            #correcto
            if user is not None:
                login(request, user)
                return redirect('inicio')

            else:
                messages.warning(request, 'Error de Autentificación')

        return render(request, 'users/login.html', {
            'title': 'Identificacion de Usuario'
        })

def logout_user(request):
    logout(request)
    return redirect('login')