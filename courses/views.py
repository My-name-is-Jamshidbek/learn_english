from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Course
from .forms import CourseForm


@login_required
def course_create(request):
    """View to create a new course."""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.created_by = request.user  # Automatically assign the current user
            course.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'staff/courses/course_form.html', {'form': form})


@login_required
def course_list(request):
    # Filter courses by the current user
    courses = Course.objects.filter(created_by=request.user)
    return render(request, 'staff/courses/course_list.html', {'courses': courses})


@login_required
def course_update(request, course_id):
    """View to update an existing course."""
    course = get_object_or_404(Course, pk=course_id)

    # Check if the current user created this course
    if course.created_by != request.user:
        raise PermissionDenied("You don't have permission to edit this course.")

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'staff/courses/course_form.html', {'form': form})


@login_required
def course_delete(request, course_id):
    """View to delete a course."""
    course = get_object_or_404(Course, pk=course_id)

    # Check if the current user created this course
    if course.created_by != request.user:
        raise PermissionDenied("You don't have permission to delete this course.")

    if request.method == 'POST':
        course.delete()
        return redirect('course_list')

    return render(request, 'staff/courses/course_confirm_delete.html', {'course': course})
