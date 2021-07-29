from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

# Create your models here.

class RecipieCategorie(models.Model):
    recipiecategorie = models.CharField(max_length=20)


    def __str__(self):
        return self.recipiecategorie



class Recipies(models.Model):
    name = models.CharField(max_length=100)
    categorie = models.ForeignKey(RecipieCategorie, on_delete=CASCADE)

    description = models.TextField()
    ingredients = models.TextField()
    one_word = models.CharField(max_length=30)

    servig_size = models.IntegerField()
    calories = models.IntegerField()
    carbohydrates = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    potassium = models.IntegerField()
    vitaminA = models.IntegerField()

    time_added = models.DateTimeField(default=timezone.now)


    main_image = models.ImageField(upload_to='main_images')
    image_first = models.ImageField(upload_to='image1')
    image_second = models.ImageField(upload_to='image2')
    image_third = models.ImageField(upload_to='image3')

    