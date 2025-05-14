from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario

def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            password = form.cleaned_data['password']
            try:
                User = Usuario.objects.get(usuario=usuario, password=password)
                return redirect('dashboard')
            except Usuario.DoesNotExist:
                error_message = "Datos invalidos"
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else: 
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def Logout_view(request):
    Logout_view(request) #Cierra la sesion del usuario
    return redirect('login')

def dashboard_view(request):
    return render(request, 'dashboard.html')

            


                

