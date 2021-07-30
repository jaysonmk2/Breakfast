from django.shortcuts import get_object_or_404, render
from .models import Recipies

# Create your views here.



def recipie_list(request):

    recipie = Recipies.objects.all()
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})


def food_filter(request):
    recipie = Recipies.objects.filter(categorie = 3)
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})

def eggs_filter(request):
    recipie = Recipies.objects.filter(categorie = 2)
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})

def drink_filter(request):
    recipie = Recipies.objects.filter(categorie = 1)
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})

def recipies_detail(request, recipie_id):
    recipie_detail = get_object_or_404(Recipies, pk= recipie_id)
    return render(request, 'details/details.html', {'detail':recipie_detail})


