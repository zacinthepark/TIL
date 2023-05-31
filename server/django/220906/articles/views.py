from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe, require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     # ArticleForm() 인스턴스 생성
#     form = ArticleForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)

@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)    # (data=request.POST)
        # 유효성 검사
        if form.is_valid():                 # form에 있는 데이터가 유효하다면
            article = form.save()           # form에 있는 데이터를 저장하고 (article을 굳이 앞에 써서 할당하는 것은 article.pk를 활용하기 위함)
            return redirect('articles:detail', article.pk)
    else:
        # new (렌더링할 페이지에게 form을 넘겨줌)
        form = ArticleForm()
    # 1) create에서 is_valid()를 통과하지 못했을 때 여기서 받음
    # 2) new에서 빈 form을 만들고 여기서 받아서 렌더링도 가능
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

    # form = ArticleForm(request.POST)
    # # 유효성 검사
    # if form.is_valid():
    #     article = form.save()
    #     return redirect('articles:detail', article.pk)
    # print(f'에러: {form.errors}')
    # context = {
    #     'form': form,
    # }
    # # return redirect('articles:new')
    # # context에 실패한 form을 넘겨줌
    # return render(request, 'articles/new.html', context)

    # 사용자의 데이터를 받아서
    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # DB에 저장
    # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2
    # article = Article(title=title, content=content)
    # article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # return render(request, 'articles/index.html')
    # return redirect('/articles/')
    # return redirect('articles:index')
    # return redirect('articles:detail', article.pk)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    # if request.method == 'POST':
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     form = ArticleForm(instance=article)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)

# create와 다른 점은 instance(수정하고자 하는 현재 게시글)가 있고 없고의 차이
# 모델을 담고 있는 ArticleForm() 인스턴스를 넘겨주어 렌더링, pk값을 위해 Article() 인스턴스도 전달
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # update (update 화면에서 제출 버튼을 눌러 update url로 POST 요청을 한 경우라면)
    if request.method == 'POST':
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        # form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid(): # form에 있는 데이터가 유효하다면
            form.save()     # form에 있는 데이터를 저장하고
            return redirect('articles:detail', article.pk)

    else:
        # edit (상세화면에서 UPDATE 버튼을 눌러 update url로 온 것이라면)
        # article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)    # 기존 해당 pk값의 게시글 내용으로 채운 form을 넘겨줌
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
