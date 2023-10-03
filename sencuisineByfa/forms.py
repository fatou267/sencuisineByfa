from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recette, Cuisine, Ingredient
from .models import UserProfile

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    pass


class MaRecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['nom', 'description', 'portions', 'utilisateur', 'ingredients', 'cuisines']

    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )

    cuisines = forms.ModelMultipleChoiceField(
        queryset=Cuisine.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'image']

