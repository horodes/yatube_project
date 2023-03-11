from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    context = {
        'posts': Post.objects.order_by('-pub_date')[:10],
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'title': group.title,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)