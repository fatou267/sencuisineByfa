import os
import django
import random
from faker import Faker
from ..models import Ingredient, Cuisine, Recette, UserProfile
from django.contrib.auth.models import User

# Configurez Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

# Initialisez Faker
fake = Faker()

# Fonction pour créer un utilisateur avec un profil
def create_user_and_profile():
    user, created = User.objects.get_or_create(username='user1')
    
    # Si l'utilisateur existe déjà, mettez à jour le profil utilisateur existant
    if not created:
        profile = UserProfile.objects.get(user=user)
        profile.bio = fake.text()
        profile.location = fake.city()
        profile.image = fake.image_url()
        profile.save()
    else:
        # Sinon, créez un nouveau profil utilisateur
        profile = UserProfile.objects.create(user=user, bio=fake.text(), location=fake.city(), image=fake.image_url())

def run():
    # Créez des utilisateurs avec des profils
    for _ in range(10):
        create_user_and_profile()

    # Créez des ingrédients fictifs
    for _ in range(20):
        Ingredient.objects.create(nom=fake.word(), unite_mesure=fake.word())

    # Créez des cuisines fictives
    cuisines = ['Française', 'Italienne', 'Mexicaine', 'Chinoise', 'Indienne', 'Japonaise']
    for cuisine in cuisines:
        Cuisine.objects.create(nom=cuisine)

    # Créez des recettes fictives
    users = User.objects.all()
    ingredients = Ingredient.objects.all()
    cuisines = Cuisine.objects.all()

    for _ in range(30):
        recette = Recette.objects.create(
            nom=fake.sentence(),
            description=fake.paragraph(),
            portions=random.randint(1, 6),
            utilisateur=random.choice(users)
        )
        recette.ingredients.set(random.sample(list(ingredients), random.randint(1, 5)))
        recette.specialites_culinaires.set(random.sample(list(cuisines), random.randint(1, 3)))

    print("Données fictives ajoutées avec succès.")

if __name__ == '__main__':
    run()
