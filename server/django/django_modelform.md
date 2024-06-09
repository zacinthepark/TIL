## ModelForm

---

- https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/

```python
class BaseModelForm(BaseForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, 
                 initial=None, error_class=ErrorList, label_suffix=None, 
                 empty_permitted=False, instance=None, use_required_attribute=None, 
                 renderer=None):
        ...
    
```

### ModelForm

<p align="center">
    <img width="600" alt="modelform" src="https://github.com/zacinthepark/TIL/assets/86648892/51bf2aee-96f8-4073-a88c-9a2904f9aab5">
</p>

- Model을 기반으로 한 Form Class
    - 사용자로부터 받는 데이터가 DB에 영향을 미치는가 여부에 따라 사용 여부 결정
    - 로그인은 사용자의 데이터를 받아 인증 과정에서만 사용하므로 Form
    - 회원가입은 유저 데이터를 추가하는 것이므로 ModelForm

### ModelForm 선언

```python
# 1
class formName(forms.ModelForm):

    class Meta:
        model = modelName
        fields = [fieldName1, fieldName2, ...]

# 2
class formName(forms.ModelForm):

    class Meta:
        model = modelName
        fields = '__all__'

# 3
class formName(forms.ModelForm):

    class Meta:
        model = modelName
        fields = exclude('fieldName1', ...)

```

### save

```python
def save(self, commit=True):
    modelInstance = modelName(**self.cleaned_data)

    if commit:
        modelInstance.save()
    
    return modelInstance

```

- DB에 새로운 레코드를 추가하는 방법
    - 모델 인스턴스를 생성한 후 `save()` 메서드 호출
    - `모델명.objects.create(필드값)` 메서드 호출
    - ModelForm의 `save()` 호출

- 데이터 유효성 검사가 끝나면 데이터를 어떤 레코드에 매핑해야할지 아는 상태로 `save()` 호출 가능

- `save(commit=False)`를 진행하면 DB에 객체를 저장하기 전 사용자 지정 처리 수행 가능
    - 예를 들어 관계가 설정된 다른 객체 저장 가능

```python
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

```

### 데이터 추가

```python
# blog/forms.py
from .models import Post

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

# blog/views.py
from .forms import PostModelForm

def post_create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # post = Post.objects.create(**form.cleaned_data)
            post = form.save(commit=False)
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            return redirect(post)
    
    else:
        form = PostModelForm()
        return render(request, 'blog/post_form.html', {'form': form})

```

### 데이터 수정

- `instance` 키워드를 통해 수정할 인스턴스 지정

```python
# blog/urls.py
urlpatterns = [
    ...
    path('update/<id>/', views.post_update, name='update'), 
    path('delete/<id>/', views.post_delete, name='delete'), 
    ...
]

# blog/views.py
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:list')
    
    else:
        form = PostModelForm(instance=post)
        return render(request, 'blog/post_update.html', {'form': form})

```

### 데이터 삭제

```python
# blog/views.py
def post_delete(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog:list')
    
    else:
        return render(request, 'blog/post_delete.html', {'post': post})

```
