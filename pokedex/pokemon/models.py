from django.db import models

# Create your models here.


# pokemon class
class Pokemon(models.Model):
    pokemon_name = models.CharField(max_length=255)
    pokemon_type = models.CharField(max_length=255)
    pokemon_number = models.CharField(max_length=3)
