# File used for routing
from django.urls import path
# Import the views from this directory
from . import views

# adds a name to the app
app_name = 'pokemon'
urlpatterns = [
    path('', views.index, name='index'),
    # show by pokemon number
    path('show/<str:pokemon_number>/', views.show, name='show'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
]
