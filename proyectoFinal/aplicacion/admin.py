from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Pelicula)
admin.site.register(Serie)
admin.site.register(Estreno)
admin.site.register(PeliculasTaquilleras)
admin.site.register(Top10Series)