from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


from django.shortcuts import render, redirect
from accounts.forms import MyLoginForm, MyRegisterForm


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, "Incorrect username or password")

    form = MyLoginForm()
    return render(request, "accounts/login.html", {"form": form})  


def logout_user(request):
    logout(request)
    return redirect("home")

def register_user(request):
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        messages.info(request, "You have entered a field incorrectly")
    else:
        form = MyRegisterForm()

    return render(request, "accounts/register.html", {"form": form})  

