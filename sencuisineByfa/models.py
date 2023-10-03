from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Modèle pour les ingrédients
class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    unite_mesure = models.CharField(max_length=50)

    def __str__(self):
        return self.nom

# Modèle pour les spécialités culinaires
class Cuisine(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

# Modèle pour les recettes
class Recette(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    portions = models.IntegerField()
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    specialites_culinaires = models.ManyToManyField(Cuisine)  # Relation avec la classe Cuisine
    image = models.ImageField(upload_to='recette_images/', blank=True, null=True)

    def __str__(self):
        return self.nom

# Modèle pour la table de liaison entre les recettes et les ingrédients
class RecipeIngredient(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2,null=True, blank=True, default=None)



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.username

    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
