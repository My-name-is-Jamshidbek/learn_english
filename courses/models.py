# models.py
from django.db import models
from ckeditor.fields import RichTextField
from accounts.models import User  # Import the correct model


class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    level = models.PositiveIntegerField()
    description = models.TextField(null=True, blank=True)
    score = models.PositiveIntegerField()

    def __str__(self):
        return f"Course {self.course_id} - Level {self.level}"

    class Meta:
        ordering = ['course_id']


class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lessons')  # Direct reference
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    lesson_title = models.CharField(max_length=255)
    content = RichTextField()  # Using CKEditor RichTextField
    score = models.BigIntegerField(blank=True, null=True)

    def __str__(self):
        return self.lesson_title


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    lesson = models.ForeignKey('Lesson', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment {self.comment_id} by {self.user.username}"
