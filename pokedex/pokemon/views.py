from django.shortcuts import render
# import djsngo httpreso=ponse
from django.http import HttpResponse, JsonResponse

# defines an index view
def index(request):
  return HttpResponse("Time to catch 'em all")

# view for showing pokemon
def show(request):
  # create a dictionary for pokemon data
  response_data = {
    'name' : 'Bulbasaur',
    'type' : 'Grass',
    'number' : '001',
  }
  return JsonResponse(response_data)

# Create your views here.
