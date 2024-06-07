## Admin

---

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

### admin url 확인 및 접속

```python
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('blog/', include('blog.urls'))
]

```

- 로컬로 접속 시 'http://127.0.0.1:8000/admin'

### admin 페이지 등록

- `appName/admin.py` 파일에 register 과정 필요

- 커스터마이징 가능

- admin에 등록한 앱은 관리자 페이지에서 데이터 조작 가능

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
