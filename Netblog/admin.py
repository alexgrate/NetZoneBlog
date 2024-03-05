from django.contrib import admin
from .models import Movie, Movie_Tag


admin.site.register(Movie_Tag)

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('Movie_Tag',) 

admin.site.register(Movie, MovieAdmin)


# Register your models here.
