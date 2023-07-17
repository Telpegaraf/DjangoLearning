from django.urls import path
from . import views

urlpatterns = [
    path('<str:rectangle>/<int:length>/<int:width>/', views.get_rectangle_area),
    path('<str:square>/<int:length>/', views.get_square_area),
    path('<str:circle>/<int:r>/', views.get_circle_area),
]