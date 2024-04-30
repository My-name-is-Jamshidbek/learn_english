from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['level', 'description', 'score', 'name']


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['lesson_title', 'content', 'score']
