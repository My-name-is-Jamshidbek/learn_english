# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Comment, Lesson
from .forms import CommentForm


@login_required
def comment_create(request, lesson_id):
    lesson = get_object_or_404(Lesson, lesson_id=lesson_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lesson = lesson  # Associate with the specified lesson
            comment.user = request.user  # Associate with the current user
            comment.save()
            return redirect('lesson_detail', lesson_id=lesson_id)
    return redirect('lesson_detail', lesson_id=lesson_id)


# @login_required
# def comment_update(request, comment_id):
#     comment = get_object_or_404(Comment, comment_id=comment_id)
#
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect('comment_list', lesson_id=comment.lesson_id)
#
#     else:
#         form = CommentForm(instance=comment)
#
#     return render(request, 'comment_form.html', {'form': form, 'comment': comment})

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, comment_id=comment_id)
    lesson_id = comment.lesson_id  # Save the lesson ID for redirection

    comment.delete()

    return redirect('lesson_detail', lesson_id=lesson_id)
