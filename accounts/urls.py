from django.urls import path
from django.contrib.auth.views import LoginView, AuthenticationForm, LogoutView
from .views import register, logout_view, view_profile

urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', view_profile, name='view_profile'),
]