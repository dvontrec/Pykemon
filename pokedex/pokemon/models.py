from django.db import models

# Create your models here.


# pokemon class
class Pokemon(models.Model):
    # adds a meta class to make sure pokemon doesnt show up as 'Pokemons'
    class Meta:
        verbose_name_plural = "pokemon"

    pokemon_name = models.CharField(max_length=255)
    pokemon_type = models.CharField(max_length=255)
    pokemon_number = models.CharField(primary_key=True, max_length=3)

    # defines a method to print pokemon as a string
    def __str__(self):
        return self.pokemon_name
