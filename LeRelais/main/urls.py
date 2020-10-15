from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url


app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("Pres", views.Pres, name="Pres"),
    path("Vous", views.Vous, name="Vous"),
    path("Agir", views.Agir, name="Agir"),
    path("Soutenir", views.Soutenir, name="Soutenir"),
    #path("Connexion", views.Connexion, name="Connexion"),
    #path("Inscription", views.Inscription, name="Inscription"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)