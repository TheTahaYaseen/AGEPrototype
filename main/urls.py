
from django import views
from django.urls import path


url_patterns = [
    path("register", views.register_view, name = "register")
]