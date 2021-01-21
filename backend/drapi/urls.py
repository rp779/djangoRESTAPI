from django.urls import path
from .views import ListTodo, DetailTodo

urlpatterns = [
    path("<int:pk>/", DetailTodo.as_view()),  # --> api/
    path("", ListTodo.as_view()),  # --> e.g. api/1
]