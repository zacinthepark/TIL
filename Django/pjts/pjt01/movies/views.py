from django.shortcuts import render, redirect
from movies.models import Movie

# Create your views here.

# 전체 영화 목록 페이지 렌더링
# 전체 영화 데이터 조회 및 index.html 렌더링
def index(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }

    return render(request, 'movies/index.html', context)

# 새로운 영화 생성 페이지 렌더링
# 장르 데이터 제공 및 new.html 렌더링
def new(request):
    return render(request, 'movies/new.html')

# 단일 영화 데이터 저장
# 새로운 영화 데이터 저장 및 detail 페이지로 redirect
def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')

    movie = Movie(title=title, audience=audience, release_date=release_date, genre=genre, score=score, poster_url=poster_url, description=description)
    movie.save()

    return redirect('movies:detail', movie.pk)

# 영화 상세 페이지 렌더링
# 단일 영화 데이터 조회 및 detail.html 렌더링
def detail(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movies/detail.html', context)

# 영화 수정 페이지 렌더링
# 수정 대상 영화 데이터 조회 및 edit.html 렌더링
def edit(request, pk):
    movie = Movie.objects.get(pk=pk)
    context = {
        'movie': movie
    }

    return render(request, 'movies/edit.html', context)

# 단일 영화 데이터 수정
# 영화 데이터 수정 및 detail 페이지로 redirect
def update(request, pk):
    movie = Movie.objects.get(pk=pk)

    movie.title = request.POST.get('title')
    movie.audience = request.POST.get('audience')
    movie.release_date = request.POST.get('release_date')
    movie.genre = request.POST.get('genre')
    movie.score = request.POST.get('score')
    movie.poster_url = request.POST.get('poster_url')
    movie.description = request.POST.get('description')

    movie.save()

    return redirect('movies:detail', movie.pk)

# 단일 영화 데이터 삭제
# 단일 영화 데이터 삭제 및 index 페이지로 redirect
def delete(request, pk):
    movie = Movie.objects.get(pk=pk)
    movie.delete()

    return redirect('movies:index')
