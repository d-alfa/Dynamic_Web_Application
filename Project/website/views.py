
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth.hashers import make_password

from .models import CustomUser

def index_view(request):
    return render(request, "website/index.html")

def sign_up_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password_1 = request.POST.get("password_1")
        password_2 = request.POST.get("password_2")

        if password_1 != password_2:
            messages.error(request, "Passwords do not match")
            return render(request, "website/sign_up.html")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "website/sign_up.html")    

        hashed_password = make_password(password_1)

        new_user = CustomUser(username=username, password=hashed_password)
        new_user.save()

        return redirect("log_in")

    return render(request, "website/sign_up.html")

@never_cache
def log_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid log in credentials")

    storage = messages.get_messages(request)
    storage.used = True

    return render(request, "website/log_in.html")

def home_view(request):
    return render(request, "website/home.html")