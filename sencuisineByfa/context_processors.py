from .models import Cuisine

def cuisines_menu(request):
    cuisines = Cuisine.objects.all()
    return {'cuisines': cuisines}