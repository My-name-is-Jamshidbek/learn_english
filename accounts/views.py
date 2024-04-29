# views.py

from django.views.decorators.http import require_POST
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import UserProfile, StaffProfile
from .forms import UserProfileForm, StaffProfileForm
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


@login_required
def view_profile(request):
    user = request.user
    if user.is_staff:
        profile = get_object_or_404(StaffProfile, user=user)
        form_class = StaffProfileForm
        template_name = 'accounts/staff_profile.html'
    else:
        profile = get_object_or_404(UserProfile, user=user)
        form_class = UserProfileForm
        template_name = 'accounts/user_profile.html'

    if request.method == 'POST':
        form = form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')

    else:
        form = form_class(instance=profile)

    return render(request, template_name, {'form': form})
