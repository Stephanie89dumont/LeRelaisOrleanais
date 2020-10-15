from django.db import models
from django.contrib.auth.models import AbstractUser



class Utilisateur(AbstractUser):
    """Contain user information."""
    administrateur = models.BooleanField(default=False)

#creer une commande personnalisée pour un utilisateur admin