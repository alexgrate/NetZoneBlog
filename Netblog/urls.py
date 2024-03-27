from django.urls import path, reverse
from . import views

urlpatterns = [
    path('', views.home, name='Netblog-Home'),
    path('NetBlog/Movies', views.movies, name='Netblog-movies'),
    path('NetBlog/Anime', views.anime, name='Netblog-animes'),
    path('NetBlog/Search', views.search, name='Netblog-Search'),
    path('NetBlog/<str:id>', views.pages, name='Netblog-Pages'),
    path('NetBlog/<str:id>', views.pages, name='Netblog-Pagess'),
    path('NetBlog/Category/<str:movie_type>', views.categories, name='Netblog-Category'),
    path('NetBlog/Tag/Category/<str:name>', views.tag_categories, name= 'Netblog-Tags-Categories'),
    path('NetBlog/Date/Category/<str:movie_date>', views.date_categories, name= 'Netblog-Date-Categories'),
    path('NetBlog/Season/Category/<str:movie_title>', views.seasons_categories, name= 'Netblog-Season-Categories'),
]
