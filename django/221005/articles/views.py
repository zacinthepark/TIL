from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, HttpResponseForbidden

from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 댓글 출력을 위한 역참조
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


# @require_POST
# def delete(request, pk):
#     article = Article.objects.get(pk=pk)
#     # 인증된 유저이면서
#     if request.user.is_authenticated:
#         # 본인이 작성한 게시글만 삭제할 수 있도록 함
#         if request.user == article.user:
#             article.delete()
#             return redirect('articles:index')
#     return redirect('articles:detail', article.pk)


@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user.is_authenticated:       # 인증된 유저이면서 (통과하지 못할 시 401 Unauthorized 반환)
        if request.user == article.user:    # 본인이 작성한 게시글만 삭제할 수 있도록 함 (다르다면 403 Forbidden 반환)
            article.delete()
            return redirect('articles:index')
        return HttpResponseForbidden()
    return HttpResponse(status=401)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # 다른 사람의 글을 수정하려고 하면 메인 페이지로 리다이렉트
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            # form = ArticleForm(data=request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_POST
# 해당 게시글의 pk값을 기반으로 댓글을 데이터베이스에 추가
def comments_create(request, pk):
    if request.user.is_authenticated:       # 인증된 사용자만 댓글 쓸 수 있도록 제한
        article = Article.objects.get(pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article       # article_id를 넣어줌
            comment.user = request.user     # user_id를 넣어줌
            comment.save()
        # 출력은 detail page에게 맡김
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')


@require_POST
# [2] url을 통해 article_pk를 받는 방법 (url의 일관성을 위해 이 방법을 선택했음)
def comments_delete(request, article_pk, comment_pk):
    # 로그인된 사용자가 아니라면 삭제 불가
    if request.user.is_authenticated:
        comment = Comment.objects.get(pk=comment_pk)
        # [1] 돌아갈 게시글의 pk를 받는 방법 중 하나
        # article_pk = comment.article.pk
        # 본인 글이어야 삭제 가능 (로직)
        if request.user == comment.user:
            comment.delete()
        return redirect('articles:detail', article_pk)
