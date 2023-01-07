from django.shortcuts import render
from django.http import HttpResponse


# Главная страница
def index(request):    
    return HttpResponse('<html><body><h1>YAtube main page</h1></body></html>')


# Посты, отфильтрованные по группам
def group_posts(request, slug):
    return HttpResponse(f'Posts by groups: <h1>{slug}</h1>')
