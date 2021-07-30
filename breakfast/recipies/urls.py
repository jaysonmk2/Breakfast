from django import urls
from django.urls import path
from .views import recipie_list, recipies_detail


app_name= "breakfast"

urlpatterns = [
    path('', recipie_list, name="recipies"),
    path('<int:recipie_id>', recipies_detail, name='detail')
]
