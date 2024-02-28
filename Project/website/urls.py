
from django.urls import path
from website import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("signup/", views.sign_up_view, name="sign_up"),
    path("login/", views.login_view, name="log_in"),
    path("home/", views.home_view, name="home"),
]