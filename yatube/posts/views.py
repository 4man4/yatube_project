# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def index(request):
    """Главная страница."""
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'index.html')
    title = 'Последние обновления на сайте'
    content = Post.objects.order_by('-pub_date')[:10]
    context = {
        'title': title,
        'content': content,
    }
    return render(request, template, context)


def group_posts(request, slug):
    """Посты, отфильтрованные по группам."""
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'group_list.html')
    group = get_object_or_404(Group, slug=slug)
    title = f'Записи сообщества {group.title}.'
    content = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'group': group,
        'title': title,
        'content': content,
    }

    return render(request, template, context)
