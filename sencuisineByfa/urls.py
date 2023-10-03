from django.urls import path

from . import views

app_name = "sencuisineByfa"
urlpatterns = [
    path('', views.recetteListes, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('recette/<int:pk>/', views.RecetteDetailView.as_view(), name='recette-detail'),
    path('recettes/', views.recetteListes , name="listes"),
    path('cuisine/<int:cuisine_id>/', views.recettes_par_cuisine, name='recettes_par_cuisine'),
    path('about/', views.about, name='about'),
    path('ajouter_recette/', views.ajouter_recette, name='ajouter_recette'),
    path('profile/', views.profile, name='profile'),
]