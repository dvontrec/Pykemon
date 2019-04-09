from django.contrib import admin

# Register your models here.
from .models import Pokemon


# registers the pokemon model so it can be edited from the admin console
admin.site.register(Pokemon)
