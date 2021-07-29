from django import urls
from django.urls import path
from .views import recipie_list


app_name= "breakfast"

urlpatterns = [
    path('', recipie_list, name="recipies")
]
