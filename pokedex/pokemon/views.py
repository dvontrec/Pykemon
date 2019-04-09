from django.shortcuts import render
# import django httpresponse
from django.http import HttpResponse, JsonResponse
from .models import Pokemon
# Create your views here.


# defines an index view
def index(request):
    pokemon_list = Pokemon.objects.order_by('pokemon_number')
    output = ', '.join([p.pokemon_name for p in pokemon_list])
    return HttpResponse(output)


# view for showing pokemon
def show(request, pokemon_number):
    response = "This is the pokemon %s"
    return HttpResponse(response % pokemon_number)
