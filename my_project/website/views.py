from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

# Create your views here.


def home(request):
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
        return render(request, "home.html", {})


# def login_user(request):
#     pass


def logout_user(request):
    pass
