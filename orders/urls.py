from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("registration_attempt", views.registration_attempt, name="registration_attempt"),
    path("add_item_to_cart", views.add_item_to_cart, name="add_item_to_cart"),
    path("view_cart", views.view_cart, name="view_cart")
]
