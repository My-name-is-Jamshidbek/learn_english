from django import forms
from .models import Course, Lesson
from .models import Comment
from ckeditor.widgets import CKEditorWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())  # Using CKEditor in the form

    class Meta:
        model = Lesson
        fields = ['lesson_title', 'content', 'score']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']  # Only include text for creation and


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['level', 'description', 'score', 'name']
