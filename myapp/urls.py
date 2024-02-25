from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Define the URL pattern for the app's views
]