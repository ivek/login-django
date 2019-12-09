from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .form import RegisterForm
# Create your views here.


def user_add(request):
    return render(request, 'users/users_index.html', {'message': 'prueba desde views'})


def login_user(request):
    if request.user.is_authenticated:
         return redirect('users_add')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('users_add')

        else:
            messages.error(request, 'Usuario o contraseña no valido')

    return render(request, 'users/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')


def register_user(request):
    if request.user.is_authenticated:
         return redirect('users_add')

    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        new_user = form.save()

        if new_user:
            login(request, new_user)
            messages.success(request, 'Usuario creado exitosamente')
            return redirect('users_add')

    return render(request, 'users/register.html', {'form': form

                                                   })
