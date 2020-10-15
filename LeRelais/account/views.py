"""Contains function used for views app account."""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import Signin, Signup
from .models import Utilisateur
from django.contrib.auth.decorators import login_required


def inscription(request):
    """Display the sign up form."""
    if request.method == "POST":
        form = Signup(request.POST)
        # return redirect()
        if form.is_valid():
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = Utilisateur.objects.create_user(username, email, password)
            # user.admin = True
            user.last_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["first_name"]
            user.save()

            return redirect("account:connexion")

    else:
        return render(request, "account/Inscription.html", {"form": Signup()})


def connexion(request):
    """Display the sign in form."""
    if request.method == "POST":
        form = Signin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.administrateur == True:
                    login(request, user)
                    return redirect("account:admin")
                else:
                    login(request, user)
                    return redirect("account:my_account")
            else:
                return redirect("account:connexion_failed")
    else:
        return render(request, "account/Connexion.html", {"form": Signin()})


def connexion_failed(request):
    return render(request, "account/Connexion_failed.html", {"form": Signin()})


@login_required
def sign_out(request):
    """Allow the user to disconnect."""
    logout(request)
    return redirect("/")


@login_required
# dans la vue if request.user.admin else redirect
def my_account(request):
    """Allow the user to view their account information."""
    user = Utilisateur.objects.get(id=request.user.id)
    return render(request, "account/my_account.html", {"account": user})


def admin(request):
    admin = Utilisateur.objects.get(id=request.user.id)
    return render(request, "account/admin.html", {"account": admin})