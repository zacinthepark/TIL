## Improve Query

---

### Improve Query

- 데이터 조회 시 subquery를 줄일 수 있는 방향성을 고민
    - Django가 DB를 히트하는 수를 줄이는 것이 목표
    - ORM의 lazy한 특성으로 인해 데이터를 가져올 때 DB를 실제로 히트하는 것이 아닌, for문 등 실제로 필요할 때 DB를 히트함
    - main query를 보내는 시점에 N:1 관계에있는, N번 히트해야할 데이터를 미리 가져온다면 향후 subquery를 줄일 수 있을 것

- `annotate`, `select_related`, `prefetched_related` 등 활용

```python
# views.py

from django.shortcuts import render
from .models import Article, Comment
from django.db.models import Count

# Create your views here.
def index_1(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.annotate(Count('comment')).order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_1.html', context)

def index_2(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.select_related('user').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_2.html', context)

def index_3(request):
    # articles = Article.objects.order_by('-pk')
    articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_3.html', context)

from django.db.models import Prefetch

def index_4(request):
    # articles = Article.objects.order_by('-pk')
    # articles = Article.objects.prefetch_related('comment_set').order_by('-pk')
    articles = Article.objects.prefetch_related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    ).order_by('-pk')

    context = {
        'articles': articles,
    }
    return render(request, 'articles/index_4.html', context)
```

```html
<!-- index_1.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
{% comment %}
<p>댓글개수 : {{ article.comment_set.count }}</p>
{% endcomment %}
<p>댓글개수 : {{ article.comment__count }}</p>
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_2.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<h3>작성자 : {{ article.user.username }}</h3>
<p>제목 : {{ article.title }}</p>
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_3.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

```html
<!-- index_4.html -->

{% extends 'base.html' %} {% block content %}
<h1>Articles</h1>
{% for article in articles %}
<p>제목 : {{ article.title }}</p>
<p>댓글 목록</p>
{% for comment in article.comment_set.all %}
<p>{{ comment.user.username }} : {{ comment.content }}</p>
{% endfor %}
<hr />
{% endfor %} {% endblock content %}
```

- `annotate()`
    - `articles = Article.objects.annotate(Count('comment')).order_by('-pk')`
    - `{{ article.comment__count }}`
        - 게시글을 가져올 때 댓글 개수까지 카운팅한 값을 한번에 가져오는 것으로 개선 가능

- `select_related()`
    - 1:1 또는 N:1 참조 관계에서 쿼리 개선
    - `articles = Article.objects.select_related('user').order_by('-pk')`
        - 각 게시글마다 user를 참조하고 있음
        - 원래는 article 전체를 다 가져오는 것에서 그쳤는데
        - article을 가져오면서 article이 참조하고 있는 user id값도 처음 한번에 다 들고와서 중복적인 쿼리 요청을 1번으로 줄임

- `prefetched_prelated()`
    - M:N 또는 N:1 역참조 관계에서 쿼리 개선
    - `articles = Article.objects.prefetch_related(’comment_set’).order_by(’-pk’)`
        - 게시글 전체를 가져오면서 거기에 묶여있는 댓글 정보들도 한번에 다 들고옴

```python
articles = Articles.objects.prefetch_related(
    Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
).order_by('-pk')
```

- 기존 상황
    - 게시글 출력하면서 댓글 목록 출력
    - 댓글 출력하면서 각 댓글의 작성자를 출력
    - 100번의 쿼리

- 개선 상황
    - 댓글을 가져오면서 유저를 한번에 붙이고
    - 게시글을 가져오면서 댓글을 한번에 붙여서 가져옴
    - 2번의 쿼리로 개선
