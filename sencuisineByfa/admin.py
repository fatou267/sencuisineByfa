from django.contrib import admin
from .models import Cuisine, Recette, RecipeIngredient,Ingredient
# Register your models here.

admin.site.register(RecipeIngredient)
admin.site.register(Recette)
admin.site.register(Ingredient)
admin.site.register(Cuisine)