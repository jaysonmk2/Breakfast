from django.contrib import admin
from . import models





class RecipiesCategorieAdmin(admin.ModelAdmin):
    list_display=('recipiecategorie','id')


class RecipiesAdmin(admin.ModelAdmin):
    exclude= ('time_added',)
    list_display=('name', 'categorie')
# Register your models here.



admin.site.register(models.RecipieCategorie,RecipiesCategorieAdmin)
admin.site.register(models.Recipies, RecipiesAdmin)