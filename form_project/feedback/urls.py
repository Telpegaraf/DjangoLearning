from django.contrib import admin
from django.urls import path
from .views import update_feedback, FeedbackView, DoneView, ListFeedbackView, DetailFeedback, FeedbackViewUpdate

urlpatterns = [
    path('done', DoneView.as_view()),
    path('list', ListFeedbackView.as_view()),
    path('detail/<int:pk>', DetailFeedback.as_view()),
    path('update/<int:pk>', FeedbackViewUpdate.as_view()),
    path('', FeedbackView.as_view()),
    path('<int:id_feedback>', update_feedback)
]