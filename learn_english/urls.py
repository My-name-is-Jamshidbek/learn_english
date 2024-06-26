"""
URL configuration for learn_english project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('staff/', include('pages.staff_urls')),
    path('account/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('', include('pages.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
