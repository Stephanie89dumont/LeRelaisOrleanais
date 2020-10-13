from django.db import models

class Utilisateur(models.Model):
	nomfamille = models.CharField(max_length=200)
	prenom = models.CharField(max_length=200)
	email = models.EmailField(max_length=100)
	codepostal = models.IntegerField(null=True) # null=True -> champ optionnel pour l'utilisateur
	mdp = models.CharField(max_length=20) # À MODIFIER

	def __str__(self):
		return self.nomfamille
	

class Benevole(models.Model):
	available = models.BooleanField(default=True) # par défaut le bénévoles qui s'inscrit est disponible
	grade = models.IntegerField()
	utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)

	

class Donateur(models.Model):
	niveau : models.CharField(max_length=200) # occasionel, regulier
	utilisateur = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)

	def __str__(self):
		return self.niveau

#class Grade(models.Model): # UTILE ?
#	pass


class Mission(models.Model):
	titre = models.CharField(max_length=200) # Restauration, Hygiène, Herbergement, AideAdmin, Animation
	benevole = models.ManyToManyField(Benevole, related_name='missions', blank=True) # verifier Blank

	def __str__(self):
		return self.titre


class Article(models.Model):
	titre = models.CharField(max_length=200)
	contenu = models.CharField(max_length=2000)
	photo = models.URLField()

	def __str__(self):
		return self.titre

		