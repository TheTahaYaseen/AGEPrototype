
from . import views
from django.urls import path


urlpatterns = [
    path("register", views.register_view, name = "register"),
    path("login", views.login_view, name = "login"),
]