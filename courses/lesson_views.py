# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson, Course
from .forms import LessonForm


@login_required
def lesson_detail(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    return render(request, 'lesson_detail.html', {'lesson': lesson})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Lesson, Course
from .forms import LessonForm


@login_required
def lesson_create(request, course_id):
    # Fetch the course object
    course = get_object_or_404(Course, course_id=course_id)

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.course = course  # Associate the lesson with the specified course
            lesson.created_by = request.user  # Ensure `User` instance linkage
            lesson.save()
            return redirect('lesson_list', course_id=course_id)

    else:
        form = LessonForm()

    return render(request, 'staff/lessons/lesson_form.html', {'form': form, 'course': course})


@login_required
def lesson_update(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('lesson_list', course_id=lesson.course.pk)
    else:
        form = LessonForm(instance=lesson)

    return render(request, 'staff/lessons/lesson_form.html', {'form': form, 'course': lesson.course})


@login_required
def lesson_delete(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)
    if request.method == 'POST':
        lesson.delete()
        return redirect('lesson_list', course_id=lesson.course.pk)

    return render(request, 'staff/lessons/lesson_confirm_delete.html', {'lesson': lesson})


@login_required
def lesson_list(request, course_id):
    # Fetch the course object
    course = get_object_or_404(Course, course_id=course_id)

    # Filter lessons belonging to this course
    lessons = Lesson.objects.filter(course=course)

    return render(request, 'staff/lessons/lesson_list.html', {'course': course, 'lessons': lessons})
