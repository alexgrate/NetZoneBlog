from django.db import models
from PIL import Image


class Movie_Tag(models.Model):
    name = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    Movie_Title = models.CharField(max_length = 100)
    Movie_Season = models.CharField(max_length = 15, blank=True)
    Movie_Episode = models.CharField(max_length = 15, blank=True)
    Movie_Body = models.TextField(max_length = 350)
    Movie_Date = models.DateField(auto_now_add = True)
    Movie_Trailer = models.CharField(max_length = 1000)
    Movie_Type = models.CharField(max_length= 350)
    Movie_Download_Link = models.CharField(max_length= 1000)
    Movie_Subtitle_Download_Link = models.CharField(max_length= 1000, blank=True, default = '')
    Movie_Img = models.ImageField(upload_to= 'images', default=' ')
    Movie_views = models.IntegerField(default=0)
    Movie_Tag = models.ManyToManyField(Movie_Tag)

    
    def __str__(self): 
        return f"{self.Movie_Title} - {self.Movie_Season} - {self.Movie_Episode}"
    
    def save(self):
        super().save()
        
        img = Image.open(self.Movie_Img.path)
        if img.height > 100 or img.width > 100:
            output_size = (853, 1250)
            img.thumbnail(output_size)
            img.save(self.Movie_Img.path)


