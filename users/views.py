from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import CustomUserCreationForm

def register(request):
    if request.method == 'POST':
        register_form = CustomUserCreationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            user_name = register_form.cleaned_data.get('user_name')

            messages.success(request, f'¡Listo, {user_name}! Ahora podés iniciar tu sesión')
            return redirect('login')
    else:
        register_form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'rForm' : register_form})


def myProfile(request):
    return render(request, 'users/profile.html')