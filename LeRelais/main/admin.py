from django.contrib import admin

from .models import Utilisateur, Benevole, Donateur, Mission, Article

admin.site.register(Utilisateur)
admin.site.register(Benevole)
admin.site.register(Donateur)
admin.site.register(Mission)
admin.site.register(Article)