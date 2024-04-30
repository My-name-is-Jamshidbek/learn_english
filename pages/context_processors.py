from courses.models import Course


def base_context(request):
    context = {
        'courses': Course.objects.all(),
    }
    return context
