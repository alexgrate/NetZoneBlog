from django.shortcuts import render
from .models import Movie, Movie_Tag
import random
from django.db.models import Q
from django.http import JsonResponse, HttpResponse
from django.template.defaultfilters import truncatewords
from django.urls import reverse
from django.core.paginator import Paginator

def home(request):
    movies = Movie.objects.filter(Movie_Type = 'Movie').order_by('-Movie_Date')
    
    movie_cafes = list(Movie.objects.all().order_by('-Movie_Date'))
    random.shuffle(movie_cafes)
    
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    
    animes = Movie.objects.filter(Movie_Type = 'Anime').order_by('-Movie_Date')[0:7]
    total_animes = Movie.objects.filter(Movie_Type = 'Anime').count()
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    horrors = Movie.objects.filter(Movie_Tag__name = 'Horror').order_by('-Movie_Date')
    
    romantics = list(Movie.objects.filter(Movie_Tag__name = 'Romance').order_by('-Movie_Date'))
    random.shuffle(romantics)
    paginator = Paginator(romantics, 6)
    page_number = request.GET.get('page')
    romantics = paginator.get_page(page_number)
    
    model = {
        'movies' : movies,
        'movie_cafes' : movie_cafes,
        'most_viewed_movies' : most_viewed_movies,
        'animes' : animes,
        'total_animes' : total_animes,
        'tags' : tags,
        'actions' : actions,
        'horrors' : horrors,
        'romantics' : romantics
    }
    return render(request, 'home.html', model)

def load_more(request):
    total_item = int(request.GET.get('total_anime'))
    limit = 2
    animes = list(Movie.objects.filter(Movie_Type='Anime').order_by('-Movie_Date')[total_item: total_item+limit])
    data = {
        'animes' : []
    }
    
    for anime in animes:
        truncated_body = truncatewords(anime.Movie_Body, 15)  # Truncate Movie_Body to 15 words
        anime_data = {
            'Movie_Img' : anime.Movie_Img.url,
            'Movie_Type' : anime.Movie_Type,
            'Movie_Title' : anime.Movie_Title,
            'Movie_Season' : anime.Movie_Season,
            'Movie_Episode' : anime.Movie_Episode,
            'Movie_Body' : truncated_body,
            'id' : anime.id,
            'Netblog_category_link': reverse('Netblog-Category', kwargs={'movie_type': anime.Movie_Type}),
            'Netblog_pages_link' : reverse('Netblog-Pages', kwargs={'id': anime.id}),
            'Netblog_season_categories_link' : reverse('Netblog-Season-Categories', kwargs={'movie_title' : anime.Movie_Title}),
        }
        data['animes'].append(anime_data)
    return JsonResponse(data=data)  

def pages(request, id):
    movie = Movie.objects.get(id = id)
    tags = Movie_Tag.objects.all()
    
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    movie_type = movie.Movie_Type
    movie_title = movie.Movie_Title
    
    # Increment the views count
    movie.Movie_views = movie.Movie_views + 1
    movie.save()
    
    next_movie = Movie.objects.filter(Movie_Type=movie_type, id__gt=movie.id).order_by('id').first()    
    prev_movie = Movie.objects.filter(Movie_Type=movie_type, id__lt=movie.id).order_by('-id').first()
    
    if next_movie is None:
        next_movie = Movie.objects.filter(Movie_Type=movie_type).order_by('id').first()
    
    # If prev_movie is None, loop back to the last movie
    if prev_movie is None:
        prev_movie = Movie.objects.filter(Movie_Type=movie_type).order_by('-id').first()
        
    similar_title_movies = Movie.objects.filter(Q(Movie_Title__icontains=movie_title) & ~Q(id=movie.id))
    if similar_title_movies.exists():
        movie_relateds = similar_title_movies.order_by('Movie_Title')
    else:
        # Fetch related movies based on movie_type if no similar titles found
        movie_relateds = Movie.objects.filter(Movie_Type__icontains=movie_type).exclude(id=movie.id).order_by('Movie_Type')
        
    paginator = Paginator(movie_relateds, 5)
    page_number = request.GET.get('page')
    movie_relateds = paginator.get_page(page_number)
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie' : movie,
        'most_viewed_movies' : most_viewed_movies,
        'next_movie': next_movie,
        'prev_movie' : prev_movie,
        'movie_relateds': movie_relateds,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'pages.html', model)

def categories(request, movie_type):
    movie_cafes = list(Movie.objects.all().order_by('-Movie_Date')) 
    random.shuffle(movie_cafes)
    
    categories = Movie.objects.filter(Movie_Type=movie_type).order_by('-Movie_Date')
    paginator = Paginator(categories, 7)   
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number) 
    
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'movie_type' : movie_type,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'categories.html', model)

def tag_categories(request, name):
    movie_cafes = list(Movie.objects.all().order_by('-Movie_Date')) 
    random.shuffle(movie_cafes)
        
    
    categories = Movie.objects.filter(Movie_Tag__name=name).order_by('-Movie_Date')
    paginator = Paginator(categories, 7)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)

    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'name' : name,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'tagCategory.html', model)

def date_categories(request, movie_date):
    movie_cafes = list(Movie.objects.all().order_by('-Movie_Date'))  
    random.shuffle(movie_cafes)
        
    
    categories = Movie.objects.filter(Movie_Date = movie_date).order_by('-Movie_Date')
    paginator = Paginator(categories, 7)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)

    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'movie_date' : movie_date,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'dateCategory.html', model)

def seasons_categories(request, movie_title):
    movie_cafes = list(Movie.objects.all().order_by('-Movie_Date')) 
    random.shuffle(movie_cafes)
        
    
    categories = Movie.objects.filter(Movie_Title = movie_title).order_by('Movie_Season', 'Movie_Episode')[:5]
    paginator  = Paginator(categories, 7)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
    
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'movie_season' : movie_title,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'seasonsCategory.html', model)

def movies(request):
    movie_cafes = list(Movie.objects.filter(Movie_Type='Anime').order_by('-Movie_Date')[:5])
    random.shuffle(movie_cafes)
            
        
    categories = Movie.objects.filter(Movie_Type = 'Movie').order_by('-Movie_Date')
    paginator  = Paginator(categories, 7)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
        
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
        
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
    
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'movies.html', model)

def anime(request):
    movie_cafes = list(Movie.objects.filter(Movie_Type='Movie').order_by('-Movie_Date')[:5])
    random.shuffle(movie_cafes)
            
        
    categories = Movie.objects.filter(Movie_Type='Anime').order_by('-Movie_Date')
    paginator  = Paginator(categories, 7)
    page_number = request.GET.get('page')
    categories = paginator.get_page(page_number)
        
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]
        
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)
        
    model = {
        'movie_cafes' : movie_cafes,
        'categories' : categories,
        'most_viewed_movies' : most_viewed_movies,
        'tags' : tags,
        'actions' : actions
    }
    return render(request, 'animes.html', model)

def search(request):
    most_viewed_movies = Movie.objects.all().order_by('-Movie_views')[:5]    
    
    tags = Movie_Tag.objects.all()
    
    actions = list(Movie.objects.filter(Movie_Tag__name = 'Action').order_by('-Movie_Date')[:6])
    random.shuffle(actions)

    if request.method == 'POST':
        searched = request.POST['searched']
        searched_movies = Movie.objects.filter(Movie_Title__contains = searched)
        
        model = {'most_viewed_movies' : most_viewed_movies,'tags' : tags, 'actions' : actions, 'searched' : searched, 'searched_movies' : searched_movies}
        return render(request, 'search.html', model)
    else:
        model = {'most_viewed_movies' : most_viewed_movies,'tags' : tags, 'actions' : actions}
        return render(request, 'search.html', model)
