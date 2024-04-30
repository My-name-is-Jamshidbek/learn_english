from django.urls import path
from .views import course_create, course_list, course_update, course_delete

urlpatterns = [
    path('', course_list, name='course_list'),
    path('create/', course_create, name='course_create'),
    path('<int:course_id>/', course_detail, name='course_detail'),
    path('<int:course_id>/edit/', course_update, name='course_update'),
    path('<int:course_id>/delete/', course_delete, name='course_delete'),
]
