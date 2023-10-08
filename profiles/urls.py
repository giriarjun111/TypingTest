# exercises/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'),
    path('<int:exercise_id>/', views.exercise_detail, name='exercise_detail'),
]
