from django.http import HttpResponse
from django.shortcuts import render
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Главная страница
def index(request):
    template = os.path.join(BASE_DIR, 'templates', 'posts', 'index.html')
    # template = 'posts\index.html'
    return render(request, template)


# Посты, отфильтрованные по группам
def group_posts(request, slug):
    return HttpResponse(f'Posts by groups: <h1>{slug}</h1>')
