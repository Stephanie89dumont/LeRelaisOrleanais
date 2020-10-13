from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, "main/index.html")


def Pres(request):
    return render(request, "main/Pres.html")


def Vous(request):
    return render(request, "main/Vous.html")


def Agir(request):
    return render(request, "main/Agir.html")


def Soutenir(request):
    return render(request, "main/Soutenir.html")


def Connexion(request):
    return render(request, "main/Connexion.html")


def Inscription(request):
    return render(request, "main/Inscription.html")
