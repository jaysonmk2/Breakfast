from django.urls import path
from .views import Home

app_name='breakfasth'
urlpatterns = [
    path('', Home, name='home')
]
