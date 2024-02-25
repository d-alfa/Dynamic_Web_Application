
from django.urls import path
from website import views

urlpatterns = [
    path("", views.register_view, name="register"),
    path("registration/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("home/", views.home_view, name="home"),
]