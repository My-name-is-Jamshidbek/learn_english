# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, StaffProfile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'country', 'bio', 'total_score']


class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'country', 'bio', 'education', 'experience']
