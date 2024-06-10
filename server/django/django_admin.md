## Admin

---

- https://docs.djangoproject.com/en/4.2/ref/contrib/admin/
- https://github.com/django/django/blob/main/django/contrib/admin/options.py
- https://docs.djangoproject.com/en/4.2/ref/contrib/admin/#modeladmin-options

### admin 앱 등록

```python
INSTALLED_APPS = [
    'django.contrib.admin', 
    'django.contrib.auth', 
    'django.contrib.conttenttypes', 
    'django.contrib.sessions', 
    'django.contrib.messages', 
    'django.contrib.staticfiles', 
    'blog.apps.BlogConfig'
]

```

### admin 계정 생성

- `python manage.py createsuperuser`
    - username, password 입력
    - email은 선택사항

### admin url 등록 및 접속

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('blog/', include('blog.urls'))
]

```

- 로컬로 접속 시 'http://127.0.0.1:8000/admin'

### 모델 등록

- `appName/admin.py` 파일에 register 과정 필요
    - `admin.site.register(modelName)` 기본 등록
    - 클래스 선언 후 `admin.site.register(modelName, className)`
    - 클래스 선언 시 `@admin.register(modelName)` 데코레이터 활용

- admin에 등록한 앱은 관리자 페이지에서 데이터 조작 가능

### ModelAdmin Options

- list display options
    - `list_display`: 모델 인스턴스 목록에서 보여줄 필드 지정
    - `list_display_links`: 모델 인스턴스 목록에서 보여지는 필드명 중 해당 모델 인스턴스 정보로 이동하는 링크로 설정할 필드 지정
    - `ordering`: 모델 인스턴스 목록 정렬 기준 필드 지정
    - `list_filter`: 모델 인스턴스 목록을 필터링할 필드 지정
    - `search_fields`: 검색 대상이 될 필드 지정
    - `list_per_page`: pagination에서 한 page 당 보여줄 목록 길이

- customized display value
    - 모델의 필드 외에 관리자가 정의하여 추가로 보여줄 값 지정
    - `def methodName(self, obj): return value`를 통해 관리자 정의 값을 반환하는 메서드 선언
        - 메서드명은 `list_display` 속성에 지정할 이름
        - `obj`는 모델 인스턴스로, 관리자 정의 값을 위한 메서드는 목록에서 인스턴스가 출력될 때마다 자동으로 호출
        - 반환값은 목록 화면에 표시되는 값
    - `methodName.short_description`을 통해 관리자 정의 값을 표시할 때 사용할 제목 지정

- actions
    - 모델에 취할 action method를 설정
    - `def funcName(modeladmin, request, queryset): ...`
        - action method는 action 창에서 기능을 선택 후 실행 버튼을 누를 때 호출됨
        - 이 때 3개의 인자가 전달되는데 3번째로 전달되는 인자가 선택된 인스턴스들을 포함하고 있는 QuerySet 객체
        - 함수의 body에서 선택한 QuerySet 객체를 대상으로 일괄처리할 기능을 구현
    - ModelAdmin 클래스의 `actions` 속성에 추가
    - `funcName.short_description`을 통해 action 창에서 해당 action 함수를 선택하기 위한 문자열 작성

- fieldsets
    - 모델 인스턴스 세부 정보에서 필드를 어떻게 구분할지 지정

- inlines
    - 모델 인스턴스 세부 정보에서 표시할 다른 모델 지정
    - 출력 형태에 따라 `TabularInline`, `StackedInline`이 있음

```python
# blog/models.py
from django.db import models
from django.urls import reverse

class Post(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=250)
    tag = models.ManyToManyField('Tag', blank=True)
    ip = models.GenericIPAddressField(null=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:detail', args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=20)
    message = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

```

```python
# blog/admin.py
from django.contrib import admin
from .models import Post, Comment, User, Profile, Tag

# admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tag)

class CommentInline(admin.StackedInline):
    model = Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body']
    list_display_links = ['id', 'title']
    ordering = ['title']
    list_filter = ['tag']
    search_fields = ['body']
    list_per_page = 3

    fieldsets = (
        ('기본정보', {'fields': ('title', 'body')}), 
        ('기타정보', {'fields': ('tag', 'ip')})
    )

    inlines = (CommentInline)

admin.site.register(Post, PostAdmin)

def make_deleted(modeladmin, request, queryset):
    queryset.update(deleted=True)

make_deleted.short_description = '선택된 comments를 삭제 상태로 설정합니다.'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message_length', 'deleted']
    actions = [make_deleted]
    
    def message_length(self, obj):
        return len(obj.message)

    message_length.short_description = '댓글 글자 수'

```
