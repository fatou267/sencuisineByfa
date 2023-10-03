from django.http import HttpResponse
# Create your views here.
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from .models import Recette, Cuisine, Ingredient
from django.views import generic
from .forms import MaRecetteForm
from .models import UserProfile
from .forms import UserProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('sencuisineByfa:index')  
    else:
        form = SignUpForm()
    return render(request, 'sencuisineByfa/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('sencuisineByfa:index') 
    else:
        form = LoginForm()
    return render(request, 'sencuisineByfa/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 


def recetteListes(request):
    #model: Recette
    recettes = Recette.objects.all()

    context = {
        'recettes': recettes,
    }
    return render(request, 'sencuisineByfa/listes.html', context)

def index(request):
    recettes = Recette.objects.all()
    cuisines = Cuisine.objects.all()

    context = {
        'recettes': recettes,
        'cuisines': cuisines,
    }

    return render(request, 'sencuisineByfa/index.html', context)



def ajouter_recette(request):
    ingredients = Ingredient.objects.all()
    cuisines = Cuisine.objects.all()

    if request.method == 'POST':
        form = MaRecetteForm(request.POST)
        if form.is_valid():
            # Traitement des nouvelles cuisines
            nouvelle_cuisine = form.cleaned_data['nouvelle_cuisine']
            if nouvelle_cuisine:
                Cuisine.objects.create(nom=nouvelle_cuisine)

            # Traitement des nouveaux ingrédients
            nouvelle_ingredient = form.cleaned_data['nouvelle_ingredient']
            if nouvelle_ingredient:
                Ingredient.objects.create(nom=nouvelle_ingredient)

            # Enregistrement de la recette
            recette = form.save()
            return redirect('sencuisineByfa:recette-detail', recette.pk)
    else:
        form = MaRecetteForm(initial={'ingredients': ingredients, 'cuisines': cuisines})

    return render(request, 'sencuisineByfa/ajouter_recette.html', {'form': form})

def recettes_par_cuisine(request, cuisine_id):
    cuisine = Cuisine.objects.get(pk=cuisine_id)
    recettes = Recette.objects.filter(specialites_culinaires=cuisine)

    context = {
        'cuisine': cuisine,
        'recettes': recettes,
    }

    return render(request, 'sencuisineByfa/recettes_par_cuisine.html', context)

def about(request):
    return render(request, 'sencuisineByfa/about.html')
 
class RecetteDetailView(generic.DetailView):
    model = Recette
    template_name = 'senCuisineByfa/detail.html'



def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'sencuisineByfa/profile.html', {'user_profile': user_profile, 'form': form})


def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile_edit.html', {'form': form})