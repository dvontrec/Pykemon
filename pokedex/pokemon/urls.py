# File used for routing
from django.urls import path
# Import the views from this directory
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('show/', views.show, name='show')
]