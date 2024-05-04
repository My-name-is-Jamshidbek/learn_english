from django.contrib import admin
from .models import Course, Lesson, Comment


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'score')  # Customize the columns shown
    search_fields = ('name',)  # Allow searching by course name

class LessonAdmin(admin.ModelAdmin):
    list_display = ('lesson_title', 'course', 'score')
    list_filter = ('course',)  # Filter options in the admin
    search_fields = ('lesson_title',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_text', 'lesson', 'user', 'comment_date')
    list_filter = ('lesson', 'user')
    search_fields = ('comment_text',)

# Register your models with these customized admin options
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Comment, CommentAdmin)
