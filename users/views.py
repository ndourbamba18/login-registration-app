from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages    
from .forms import RegistrationForm, LoginForm

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            new_password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, email=email, password=new_password)
            login(request, user)
            messages.success(request, f"Votre inscription a été bien prise en compte\nMerci de nous faire confiance")
            return redirect("login")
    else:
        form = RegistrationForm()
    return render(request, "users/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = LoginForm()

    return render(request, "users/login.html", {"form": form})
