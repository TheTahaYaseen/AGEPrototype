
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
    path("user_queries", views.user_queries_view, name = "user_queries"),
    path("delete_query/<str:primary_key>", views.delete_query_view, name = "delete_query"),
 
    path("products", views.products_view, name = "products"),
    path("create_product", views.create_product_view, name = "create_product"),
    path("product/<str:primary_key>", views.product_view, name = "product"),
    path("edit_product/<str:primary_key>", views.edit_product_view, name = "edit_product"),
    path("delete_product/<str:primary_key>", views.delete_product_view, name = "delete_product"),

    path("newsletters", views.newsletters_view, name = "newsletters"),
    path("create_newsletter", views.create_newsletter_view, name = "create_newsletter"),
    path("newsletter/<str:primary_key>", views.newsletter_view, name = "newsletter"),
    path("edit_newsletter/<str:primary_key>", views.edit_newsletter_view, name = "edit_newsletter"),
    path("delete_newsletter/<str:primary_key>", views.delete_newsletter_view, name = "delete_newsletter"),
]