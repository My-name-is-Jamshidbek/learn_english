from django.urls import path
from .views import course_create, course_list, course_update, course_delete
from .lesson_views import lesson_detail, lesson_create, lesson_update, lesson_delete, lesson_list

urlpatterns = [
    path('lessons/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('<int:course_id>/lessons/new/', lesson_create, name='lesson_create'),
    path('lessons/<int:lesson_id>/edit/', lesson_update, name='lesson_update'),
    path('lessons/<int:lesson_id>/delete/', lesson_delete, name='lesson_delete'),
    path('<int:course_id>/lessons/', lesson_list, name='lesson_list'),

    path('', course_list, name='course_list'),
    path('create/', course_create, name='course_create'),
    path('<int:course_id>/edit/', course_update, name='course_update'),
    path('<int:course_id>/delete/', course_delete, name='course_delete'),
]
