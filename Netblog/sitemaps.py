from django.contrib import sitemaps
from django.urls import reverse
from .models import Movie


class EpisodeSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.6

    def items(self):
        # Assuming you have a method to fetch episodes
        return Movie.objects.all()

    def lastmod(self, obj):
        # Assuming you have a date field for last modification
        return obj.Movie_Date

class StaticViewsSitemap(sitemaps.Sitemap):
    
    priority = 0.5
    changefreq = 'daily'
    
    def items(self):
        return [
            'Netblog-Home',
            'Netblog-movies',
            'Netblog-animes',
            'Netblog-Search',
        ]
        
    def location(self, item):
        return reverse(item)