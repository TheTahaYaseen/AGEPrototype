from django.db import IntegrityError
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

from .models import Product, ProductCategory, ProductMedia, UserQuery

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

        if not request.user.is_authenticated:
            error = "You Need To Login Before Being Able To Submit A Query!"

        else:
            subject = request.POST.get("subject")
            message = request.POST.get("message")

            user = request.user
            admin_response = None

            try:
                UserQuery.objects.create(
                    query_user = user,
                    subject = subject,
                    message = message,
                    admin_response = admin_response
                )
            except IntegrityError:
                error = "Subject Or Message Not In Correct Format!"

    context = {"error": error}  

    return render(request, "main/user_interface/contact.html", context)

def queries_view(request):
    if not request.user.is_superuser:
        return redirect("home")
    
    if request.method == "POST":
        query_id = request.POST.get("query_id")
        response = request.POST.get("response")
        
        print(query_id)
        query = UserQuery.objects.get(id = query_id)
        query.admin_response = response
        query.save()

    queries = UserQuery.objects.all()

    unresponded_queries = [query for query in queries if not query.admin_response]
    responded_queries = [query for query in queries if query.admin_response]

    context = {"unresponded_queries": unresponded_queries, "responded_queries": responded_queries}
    return render(request, "main/admin_interface/queries.html", context)

def create_product_view(request):

    form_operation = "Create"
    error = ""
    categories = ProductCategory.objects.all()

    if request.method == "POST":
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        product_category = request.POST.get('product_category')
        product_image = request.FILES.get('product_image')

        try:
            product_category, created = ProductCategory.objects.get_or_create(product_category = product_category)
        except Exception:
            error = "An Error Occured During Creation Of Product Category!"

        if not error:

            try:
                product = Product.objects.create(
                    product_name = product_name,
                    product_description = product_description,
                    product_category = product_category,
                )

                ProductMedia.objects.create(
                    product = product,
                    media_file = product_image
                )

            except Exception:
                error = "An Error Occured During Creation Of Product!"

    context = {"form_operation": form_operation, "categories": categories, "error": error}
    return render(request, "main/admin_interface/product_form.html", context)