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

    return render(request, "main/auth/register.html", context)

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

    return render(request, "main/auth/login.html", context)

def logout_view(request):

    if request.user.is_authenticated:
        logout(request)

    return redirect("home")

def home_view(request):

    context = {}

    return render(request, "main/user_interface/home.html", context)

def about_view(request):
    context = {}

    return render(request, "main/user_interface/about.html", context)


def specifications_admin_view(request):
    # Create Form 
    # Fetches All Specifications
    # Option To Update
    # Option To Delete

    if not request.user.is_superuser:
        return redirect("home")

    context = {}
    return render(request, "main/admin_interface/specifications.html", context)

def contact_view(request):
    
    error = ""

    if request.method == "POST":
        error = "Contact Functionality Not Availaible Yet!"

    context = {"error": error}  

    return render(request, "main/user_interface/contact.html", context)