from django.http import HttpResponse


def group_posts(request, slug):
    return HttpResponse(f'Список постов {slug}')
