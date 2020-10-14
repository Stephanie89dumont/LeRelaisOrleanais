"""Contains the application’s url."""
from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('', views.my_account, name='my_account'),
    path('inscription', views.inscription, name='inscription'),
    path('connexion', views.connexion, name='connexion'),
    path('sign_out', views.sign_out, name='sign_out'),
    ]