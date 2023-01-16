from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    # detail url에 필요한 파라미터 pk를 같이 넘겨줌
    return redirect('articles:detail', article.pk)

# url로부터 pk를 잘라서 같이 보내줌
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# edit 템플릿을 보여주는 view
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# 실제 데이터 수정
def update(request, pk):
    # 1. pk로 수정할 게시글을 가져온다
    article = Article.objects.get(pk=pk)
    # 2. request에서 사용자가 입력한 title과 content를 가져온다
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 3. DB에서 수정할 데이터로 조작한다
    article.save()
    # 4. 모든 조작이 끝나면 어디론가 보낸다
    return redirect('articles:detail', article.pk)
