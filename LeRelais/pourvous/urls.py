from django.urls import include, path
from . import views # import views so we can use them in urls.

app_name = 'pourvous'

urlpatterns = [
    path('pr', views.pourvs, name='pourvs'), # "/pourvous" will call the method "pourvs" in "views.py"
    path('', views.index, name='index'),
    path('Pres', views.Pres, name='Pres'),
    path('Vous', views.Vous, name='Vous'),
    path('Agir', views.Agir, name='Agir'),
    path('Soutenir', views.Soutenir, name='Soutenir'),
]