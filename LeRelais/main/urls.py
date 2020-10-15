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
    path("Donation", views.Donation, name="Donation"),
    path("Mention", views.Mention, name="Mention"),
    path("Contact", views.Contact, name="Contact"),
    path("Location", views.Location, name="Location"),
    path("Info", views.Info, name="Info"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)