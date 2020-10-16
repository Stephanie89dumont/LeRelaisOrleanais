"""Contains the application’s url."""
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.my_account, name="my_account"),
    path("", views.admin, name="admin"),
    path("inscription", views.inscription, name="inscription"),
    path("connexion", views.connexion, name="connexion"),
    path("connexion_failed", views.connexion_failed, name="connexion_failed"),
    path("sign_out", views.sign_out, name="sign_out"),
]
