from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .forms import AddCustomerForm, SignUpForm
from .models import CustomModel

# Create your views here.


def home(request):
    customers = CustomModel.objects.all()
    # Check to see if logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect("home")
        else:
            messages.error(
                request, "There was an error authenticating, please try again"
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"customers": customers})


# def login_user(request):
#     pass


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out")
    return redirect("home")


def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered!")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})


def customers(request, pk):
    if request.user.is_authenticated:
        # Look Up Records
        customer = CustomModel.objects.get(id=pk)
        return render(request, "customer.html", {"customer": customer})
    else:
        messages.success(request, "You Must Be Logged In To View That Page...")
        return redirect("home")


def delete_customer(request, pk):
    if request.user.is_authenticated:
        customer = CustomModel.objects.get(id=pk)
        if request.method == "POST":
            customer.delete()
            messages.success(request, "Customer Deleted Successfully...")
            return redirect("home")
        return render(request, "delete_customer.html")
    else:
        messages.success(request, "You Must Be Logged In To Do That...")
        return redirect("home")


def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Customer Added...")
                return redirect("home")
        return render(request, "add_customer.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")


def update_customer(request, pk):
    if request.user.is_authenticated:
        current_customer = CustomModel.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer Has Been Updated!")
            return redirect("home")
        return render(request, "update_customer.html", {"form": form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect("home")
