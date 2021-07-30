from django.shortcuts import get_object_or_404, render
from .models import Recipies

# Create your views here.



def recipie_list(request):

    recipie = Recipies.objects.all()
    return render(request, 'recipies/recipies.html', {'recipie' : recipie})


def recipies_detail(request, recipie_id):
    recipie_detail = get_object_or_404(Recipies, pk= recipie_id)
    return render(request, 'details/details.html', {'detail':recipie_detail})
