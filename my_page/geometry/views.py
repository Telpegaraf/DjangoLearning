from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def get_rectangle_area(request, length: int,width: int):
    return HttpResponse(length*width)


def get_square_area(request, length: int):
    return HttpResponse(f"вот так вот {length**2}")


def get_circle_area(request, r: int):
    return HttpResponse(r**2 * 3.14)