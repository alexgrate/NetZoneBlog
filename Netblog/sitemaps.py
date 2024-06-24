from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import Movie

class MovieSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Movie.objects.all()

    def lastmod(self, obj):
        return obj.Movie_Date
    
    def location(self, obj):
        return obj.get_absolute_url()
    
    
class MovieTypeSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.6

    def items(self):
        return Movie.objects.values_list('Movie_Type', flat=True).distinct()

    def location(self, item):
        return reverse('Netblog-Category', args=[item])
    
    
class StaticViewsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'weekly'

    def items(self):
        return ['Netblog-Home',
                'Netblog-movies',
                'Netblog-animes']

    def location(self, item):
        return reverse(item)
