
from . import views
from django.urls import path


urlpatterns = [
    path("", views.home_view, name = "home"),
    
    path("register", views.register_view, name = "register"),
    path("login", views.login_view, name = "login"),
    path("logout", views.logout_view, name = "logout"),
    
    path("about", views.about_view, name = "about"),
 
    path("contact", views.contact_view, name = "contact"),
    path("queries", views.queries_view, name = "queries"),
 
    path("create_product", views.create_product_view, name = "create_product"),
    path("products", views.products_view, name = "products"),
]