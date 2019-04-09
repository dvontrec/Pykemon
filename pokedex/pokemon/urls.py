# File used for routing
from django.urls import path
# Import the views from this directory
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # show by pokemon number
    path('show/<str:pokemon_number>', views.show, name='show')
]
