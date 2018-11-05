from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('questions/', views.QuestionListAPIView.as_view(), name='index'),
    path('questions/<int:pk>/', views.QuestionDetailAPIView.as_view(), name='detail'),
    path('choices/', views.ChoiceListAPIView.as_view()),
    path('choices/<int:pk>/', views.ChoiceDetailAPIView.as_view()),
]
