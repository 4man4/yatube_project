# from django.http import HttpResponse
from django.shortcuts import render
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Главная страница
def index(request):
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'index.html')
    return render(request, template)


# Посты, отфильтрованные по группам
def group_posts(request, slug):
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'group_list.html')
    return render(request, template)
