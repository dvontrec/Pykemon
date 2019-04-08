from django.shortcuts import render
# import djsngo httpreso=ponse
from django.http import HttpResponse

# defines an index view
def index(request):
  return HttpResponse("Time to catch 'em all")

# Create your views here.
