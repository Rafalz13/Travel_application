from django.contrib import admin
from .models import Destinations, Attractions, History
# Register your models here.

admin.site.register(Destinations)
admin.site.register(Attractions)
admin.site.register(History)
