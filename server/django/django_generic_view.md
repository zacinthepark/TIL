## Generic View

---

- https://docs.djangoproject.com/en/4.2/ref/class-based-views/base/#view
- https://github.com/django/django/tree/4.2/django/views/generic
- https://ccbv.co.uk/
- https://docs.djangoproject.com/en/4.2/ref/class-based-views/

### 클래스 기반 뷰

- `class.django.views.generic.base.View`를 상속
    - `View`는 모든 클래스형 View의 최상위 View

```python
# views.py
class MyFormView(View):
    form_class = MyForm
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process from cleaned data>
            return HttpResponseRedirect('/success/')
        return render(request, self.template_name, {'form': form})
    
    @classonlymethod
    def as_view(cls, **initkwargs):
        '''Main entry point for a request-response process.'''
        for key in initkwargs:
            ...

```

### Generic View

<p align="center">
    <img width="600" alt="generic_views" src="https://github.com/zacinthepark/TIL/assets/86648892/42920e60-8897-4734-a949-685c25621f51">
</p>

- Django에서 범용적으로 사용되는 기능을 구현해놓은 View 클래스
    - 별도의 View 구현없이 바로 사용할 수 있음
    - 필요한 경우 Generic View를 상속하여 속성과 메서드를 오버라이딩하여 커스터마이징할 수 있음

- 사용 방법
    - `as_view()` 메서드의 키워드 인자로 지정하는 방법
    - Generic View를 상속받은 클래스에서 지정하는 방법

#### as_view 인자

```python
# urls.py
from django.urls import path, reverse, reverse_lazy
from django.views.generic import *
from .models import Book

app_name ='book'

urlpatterns = [
    path('', ListView.as_view(model=Book), name='list'),
    path('detail/<pk>/', DetailView.as_view(model=Book), name='detail'),
    path('create/', CreateView.as_view(model=Book, fields='__all__'), name='create'),
    path('update/<pk>/', UpdateView.as_view(model=Book, fields='__all__'), name='update'),
    path('delete/<pk>/', DeleteView.as_view(model=Book, success_url=reverse_lazy('book:list')), name='delete')
]

```

#### Generic View 상속

```python
# urls.py
from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path('post/list/', views.ApiPostLV.as_view(), name='post_list'),
    path('post/<int:pk>/', views.ApiPostDV.as_view(), name='post_detail'),
    path('catetag/', views.ApiCateTagView.as_view(), name='catetag_list'),
    path('like/<int:pk>/', views.ApiPostLikeDV.as_view(), name='post_like'),
    path('comment/create/', views.ApiCommentCV.as_view(), name='comment_create')
]

```

```python
from django.http import JsonResponse
from django.views import View
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import BaseCreateView
from django.views.generic.list import BaseListView

from api.utils import obj_to_post, prev_next_post, obj_to_comment
from blog.models import Post, Category, Tag, Comment


class ApiPostLV(BaseListView):
    # model = Post
    paginate_by = 3

    def get_queryset(self):
        paramCate = self.request.GET.get('category')
        paramTag = self.request.GET.get('tag')
        if paramCate:
            qs = Post.objects.filter(category__name__iexact=paramCate)
        elif paramTag:
            qs = Post.objects.filter(tags__name__iexact=paramTag)
        else:
            qs = Post.objects.all()
        return qs.select_related('category').prefetch_related('tags')

    def render_to_response(self, context, **response_kwargs):
        qs = context['object_list']
        postList = [obj_to_post(obj, False) for obj in qs]

        pageCnt = context['paginator'].num_pages
        curPage = context['page_obj'].number

        jsonData = {
            'postList': postList,
            'pageCnt': pageCnt,
            'curPage': curPage,
        }

        return JsonResponse(data=jsonData, safe=True, status=200)


class ApiPostDV(BaseDetailView):
    # model = Post

    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags', 'comment_set')

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        post = obj_to_post(obj)
        prevPost, nextPost = prev_next_post(obj)

        qsComment = obj.comment_set.all()
        commentList = [obj_to_comment(obj) for obj in qsComment]

        jsonData = {
            'post': post,
            'prevPost': prevPost,
            'nextPost': nextPost,
            'commentList': commentList,
        }

        return JsonResponse(data=jsonData, safe=True, status=200)


class ApiCateTagView(View):
    def get(self, request, *args, **kwargs):
        qs1 = Category.objects.all()
        qs2 = Tag.objects.all()
        cateList = [cate.name for cate in qs1]
        tagList = [tag.name for tag in qs2]

        jsonData = {
            'cateList': cateList,
            'tagList': tagList,
        }

        return JsonResponse(data=jsonData, safe=True, status=200)


class ApiPostLikeDV(BaseDetailView):
    model = Post

    def render_to_response(self, context, **response_kwargs):
        obj = context['object']
        obj.like += 1
        obj.save()
        return JsonResponse(data=obj.like, safe=False, status=200)


class ApiCommentCV(BaseCreateView):
    model = Comment
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        comment = obj_to_comment(self.object)
        return JsonResponse(data=comment, safe=True, status=201)

    def form_invalid(self, form):
        return JsonResponse(data=form.errors, safe=True, status=400)

```
