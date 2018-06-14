from django.shortcuts import render
from .models import Cover,Movie
# Create your views here.
def index(request):
    content = {}
    return render(request, 'index.html', content)

def movie_list(request):
    movie = Movie.objects.filter(is_in_theater = True)
    movie_tops = Movie.objects.filter(is_in_theater = True)
    print(movie_tops)
    content = {}
    content['movie'] = movie[1:]
    content['movie_tops'] = movie_tops[0]
    return render(request, 'index2.html', content)

