from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
# 전체 DB 조회 및 정보 뿌려주기
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)

# 단순히 글 작성 페이지로만 넘겨줌
def new(request):
    return render(request, 'articles/new.html')

# 데이터 생성 및 저장
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')

# index 화면에서 넘어온 pk정보를 바탕으로 글 상세화면 생성
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/detail.html', context)

# 해당 상세 화면의 데이터 지워주고 index 화면으로 redirect
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')

# edit 템플릿을 보여주기
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }

    return render(request, 'articles/edit.html', context)

# edit에서 submit 버튼을 통해 update url로 이동 후 update function을 통해 받아온 정보를 바탕으로 데이터 수정 및 상세 화면으로 redirect
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 데이터 수정
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # DB 동기화
    article.save()

    # detail은 pk가 필요한 화면이므로 같이 보내줌
    return redirect('articles:detail', article.pk)
