from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
def register_view(request):

    form = UserCreationForm()
    error = ""

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("home")
        else:
            error = "An Error Occured During Registration"

    context = {"form": form, "error": error}

    return render(request, "main/register.html", context)

def login_view(request):
    
    if request.user.is_authenticated:
        return redirect("home")

    error = ""

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
            error = "User Does Not Exist"

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "An Error Occured During Login"

    context = {"error": error}

    return render(request, "main/login.html", context)

def logout_view(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect("home")

def home_view(request):

    context = {}

    return render(request, "main/home.html", context)

def about_view(request):
    context = {}

    return render(request, "main/about.html", context)
