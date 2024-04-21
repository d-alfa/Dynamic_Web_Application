
from django.urls import path
from website import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("signup/", views.sign_up_view, name="sign_up"),
    path("login/", views.log_in_view, name="log_in"),
    path("home/", views.home_view, name="home"),

    path('log_out', views.log_out, name="log_out")
]