from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts),
    path('<int:theme_post>', views.get_theme_by_number),
    path('<str:theme_post>', views.get_theme)
]