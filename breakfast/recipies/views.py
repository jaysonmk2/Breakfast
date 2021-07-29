from django.shortcuts import render
from .models import Recipies

# Create your views here.



def recipie_list(request):

    recipie = Recipies.objects.all()
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})
