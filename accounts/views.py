# views.py

from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Account created for {user.username}!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@require_POST  # This decorator makes sure the view only accepts POST requests
def logout_view(request):
    logout(request)
    return redirect('home')