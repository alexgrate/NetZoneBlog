from django.contrib.sitemaps import Sitemap
from .models import Movie

class MovieSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Movie.objects.all()

    def lastmod(self, obj):
        return obj.Movie_Date
    
    
    # Netblog/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['Netblog-Home',
                'Netblog-movies',
                'Netblog-animes']

    def location(self, item):
        return reverse(item)
