from django.contrib import admin
from .models import Movie, Movie_Tag, Episode


admin.site.register(Movie_Tag)

class MovieAdmin(admin.ModelAdmin):
    filter_horizontal = ('Movie_Tag',) 

admin.site.register(Movie, MovieAdmin)

admin.site.register(Episode)


# Register your models here.
