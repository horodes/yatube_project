from django.shortcuts import render


def group_posts(request, slug):
    context = {
        'title': 'Здесь будет информация о группах проекта Yatube',
        'slug': slug,
    }
    return render(request, 'groups/group_posts.html', context)
