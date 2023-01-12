# from django.http import HttpResponse
from django.shortcuts import render
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Главная страница
def index(request):
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'index.html')
    title = 'Последние обновления на сайте'
    content = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'content': content,
    }
    return render(request, template, context)


# Посты, отфильтрованные по группам
def group_posts(request, slug):
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'group_list.html')
    title = 'Лев Толстой – зеркало русской революции.'
    content = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
        'content': content,
    }
    return render(request, template, context)
