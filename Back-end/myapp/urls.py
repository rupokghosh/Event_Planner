from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the URL pattern for the app's views
    path("todos/", views.todos, name="Todos")
]