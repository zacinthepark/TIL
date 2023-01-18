from django.shortcuts import render
from .models import Article

# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# 사용자가 입력할 데이터 페이지만 렌더링해주면됨
def new(request):
    return render(request, 'articles/new.html')

# new page의 input에서 쏴준 request 속에 데이터가 있다
# 요청에 대한 모든 데이터는 request에 있다
# input에 정의한 name이 key
def create(request):
    # 사용자의 데이터를 받아서 DB에 저장
    # 데이터 받기
    title = request.GET.get('title')
    content = request.GET.get('content')

    # DB에 저장
    #1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    #2 (왼쪽이 DB의 필드, 오른쪽이 요청에서 받아온 변수)
    article = Article(title=title, content=content)
    article.save()

    # #3
    # Article.objects.create(title=title, content=content)

    return render(request, 'articles/create.html')