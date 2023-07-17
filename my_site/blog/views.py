from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def main1(request):
    return HttpResponse('Главная страница')


def posts(request):
    return HttpResponse('Все посты блога')


def get_theme_by_number(request, theme_post: int):
    return HttpResponse(f"Здесь содержится информация о посте под номером {theme_post}")


def get_theme(request, theme_post:str):
    return HttpResponse(f"информация о посте {theme_post}")