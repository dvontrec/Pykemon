from django.shortcuts import get_object_or_404,  render
from django.http import Http404, JsonResponse
from django.template import loader
from .models import Pokemon
# Create your views here.


# defines an index view
def index(request):
    # grabs the list of pokemon
    pokemon_list = Pokemon.objects.order_by('pokemon_number')
    # sets the context for what can be seen by the template
    context = {
        'pokemon_list': pokemon_list
    }
    # responds by rendering the index template passing in the context
    return render(request, 'pokemon/index.html', context)


# view for showing pokemon
def show(request, pokemon_number):
    # finds the pokemon by the number or returns a 404
    pokemon = get_object_or_404(Pokemon, pk=pokemon_number)
    return render(request, 'pokemon/details.html', {'pokemon': pokemon})


def new(request):
    return render(request, 'pokemon/new.html')


def create(request):
    return
