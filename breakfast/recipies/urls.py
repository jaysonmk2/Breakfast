from django import urls
from django.urls import path
from .views import eggs_filter, recipie_list, recipies_detail, food_filter,eggs_filter,drink_filter


app_name= "breakfast" 

urlpatterns = [
    path('', recipie_list, name="recipies"),
    path('Food' ,food_filter, name="food_filter"),
    path('Drink' ,drink_filter, name="drink_filter"),
    path('Eggs' ,eggs_filter, name="eggs_filter"),
    path('<int:recipie_id>', recipies_detail, name='detail'),
]
