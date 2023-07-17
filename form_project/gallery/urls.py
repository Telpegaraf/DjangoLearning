from django.contrib import admin
from django.urls import path
from . import views
# from .views import update_feedback, FeedbackView, DoneView, ListFeedbackView, DetailFeedback, FeedbackViewUpdate

urlpatterns = [
    path('load_image', views.CreateGalleryView.as_view()),
    path('list_image', views.ListGallery.as_view()),
]