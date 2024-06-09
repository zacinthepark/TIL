## Project and Apps

---

### Start Project

- 장고에서는 웹 사이트, 혹은 웹 어플리케이션을 프로젝트라고 지칭
    - 즉, 장고 프로젝트는 웹 사이트를 의미하며, 웹 사이트에는 사용자의 서비스를 처리하는데 여러 기능을 제공하며, 이 기능들을 앱이라고 지칭

- `django-admin startproject project_name`
    - 프로젝트 이름 뒤에 `.`을 붙이면 현재 디렉토리 내에 바로 프로젝트 디렉토리 생성
    - 프로젝트 이름으로 Python이나 Django에서 사용 중인 키워드 및 하이픈 사용 불가

- `manage.py`
    - 장고 프로젝트 생성 시 루트 디렉토리에 생성된 모듈로 현재 개발 중인 장고 프로젝트의 개발 과정에서 필요한 작업을 실행시켜주는 커맨드 유틸리티
    - `python manage.py <command> [options]`
    - `python manage.py --help`

#### 프로젝트 구조

- `__init__.py`
    - 패키지로 인식시키는 파일
    - Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시
    - 별도로 추가 코드를 작성하지 않음

- `asgi.py`
    - Asynchronous Server Gateway Interface
    - Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용

- `settings.py`
    - Django 프로젝트 전반에 대한 설정을 관리
    - `SECRET_KEY`는 프로젝트 고유 키 값

- `urls.py`
    - 사이트의 url과 적절한 views의 연결을 지정
    - `urlpatterns`에 어떤 url이 들어오면 어떤 처리를 하라는 것을 지정

- `wsgi.py`
    - Web Server Gateway Interface
    - Django 애플리케이션이 웹 서버와 연결 및 소통하는 것을 도움
    - 추후 배포 시에 사용

- `db.sqlite3`
    - 데이터베이스

### Start App

- `python manage.py startapp app_name`

- `settings.py` 의 `INSTALLED_APPS` 에 추가
    - local apps - third party apps - django apps 순서로 등록할 것을 권장
    - third party apps는 pip를 통해 설치한 것들

#### 어플리케이션 구조

- `admin.py`
    - 관리자용 페이지를 설정하는 곳
    - 현재 앱의 모델을 admin앱에서 사용하기 위한 설정 파일

- `apps.py`
    - 현재 앱에 대한 환경설정 파일
    - 별도로 추가 코드를 작성하지 않음

- `models.py`
    - 현재 앱에서 사용하는 모델에 대해 구현하는 파일

- `tests.py`
    - 현재 앱을 테스트하기 위한 파일
    - 테스트 코드를 작성하는 곳

- `views.py`
    - 현재 앱의 서비스 기능을 구현하는 파일

- `__init__.py`
    - 현재 디렉토리를 패키지로 인식하기 위한 파일

- `migrations`
    - 현재 앱의 models.py에 구현된 모델들에 대한 변경작업을 기록하는 파일들이 저장되는 디렉토리

### URL 설정

<p align="center">
    <img width="500" alt="dj_32" src="https://user-images.githubusercontent.com/86648892/188303775-20940db2-319d-4b7a-8647-a62a22ab5d7f.png">
</p>

- 프로젝트 폴더의 settings.py에서 `ROOT _URLCONF` 지정

- ROOT URLconf에서 `include`를 활용하여 분기 처리
    - include되는 앱의 urls.py에 urlpatterns가 작성되어있지 않으면 에러가 발생하므로 빈 리스트라도 작성

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include('blog.urls')),
    path("book/", include('book.urls')),
    path("gallery/", include('gallery.urls')),
    path("accounts/", include('accounts.urls'))
]
```

- 각 App의 URLconf에서 view 함수 분기 처리

```python
from django.urls import path 
from . import views 

app_name = 'blog'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:id>/', views.detail, name='detail'),
    path('test1/', views.test1),
    path('test2/<int:no>/', views.test2),
    path('test3/<year>/<month>/<day>/', views.test3),
    path('profile/', views.profile),
    path('tag/<id>/', views.tag_list),
    path('test7/', views.test7),
    path('new/', views.post_create, name='create'),
    path('update/<id>/', views.post_update, name='update'),
    path('delete/<id>/', views.post_delete, name='delete')
]
```

#### URL Variable Routing

- URL 문자열 일부를 view 함수의 인자로 전달

- `<type:name>`
    - type이 적혀있지 않다면 str이 기본값
    - str, int, slug, uuid, path

#### Naming URL patterns

- `path()` 함수의 `name` 인자 활용
    - 정의된 `name`은 향후 `{% url ' ' %}` DTL 태그를 활용하여 접근 가능
    - 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대경로 주소를 반환

- URL Namespace
    - urls.py 파일에서 `app_name` attribute을 작성해 URL namespace를 설정
    - `{% url 'appName:urlName' %}`을 통해 템플릿에서 접근
    - `app_name`을 지정한 이후에는 url 태그에서 반드시 'appName:urlName' 형태로 사용해야하며 그렇지 않는다면 NoReverseMatch 에러가 발생

### URL Tag

- 템플릿에서 URL 접근 시 사용
    - `{% url 'appName:pathName' %}
    - `{% url 'appName:pathName' 값1 값2 %}

- `<a href="{% url 'blog:detail' post.id %}">{{post.title}}</a>`
    - `<a hreft="/blog/{{post.id}}/">{{post.title}}</a>`와 동일

#### URL Reverse

- URL 패턴에 정의된 URL의 name을 바탕으로 역으로 URL에 접근

- URL에 접근하고, 인자를 주어 동적으로 URL 생성 가능
    - `reverse(appName:pathName)`
    - `reverse(appName:pathName, args=[값1, 값2, ...])`
    - `reverse(appName:pathName, kwargs={키1:값1, 키2:값2, ...})`

#### redirect

- 장고의 shortcuts 중 하나로 view 함수에서 사용
    - `redirect('URL')`
    - `redirect('appName:pathName')`
    - `redirect('appName:pathName', 값1, 값2)`
    - `redirect('appName:pathName, 키1=값1, 키2=값2)`

- `redirect('blog:detail', id=1)`
    - `<HttpResponseRedirect status_code=302, "text/html; charset=utf-8", url="/blog/1/">` 반환
    - 응답받은 브라우저는 해당 주소로 재요청 및 정상적으로 응답받을 시 200 status code 반환

#### get_absolute_url

- 장고 모델 객체의 절대 URL 반환에 사용
    - 객체가 생성되거나 업데이트된 후 리디렉션할 URL 지정하는데 유용
    - 일반적으로 `reverse`와 함께 사용

```python
# models.py
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

# views.py
from django.shortcuts import render, redirect

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            post = Post.objects.create(**form.cleaned_data)
            # redirect에서 내부적으로 post.get_absolute_url()한 결과로 redirect
            return redirect(post)
    else:
        form = PostForm()
        return render(request, 'blog/post_form.html', {'form': form})

```

### 추가 설정

- https://github.com/django/django/blob/main/django/conf/global_settings.py

- LANGUAGE_CODE
    - 모든 사용자에게 제공되는 번역을 결정
    - 이 설정이 적용되려면 `USE_I18N` 이 활성화(True)되어 있어야함
    - http://www.i18nguy.com/unicode/language-identifiers.html

- TIME_ZONE
    - 데이터베이스 연결의 시간대를 나타내는 문자열 지정
    - `USE_TZ` 가 True이고 이 옵션이 설정된 경우 데이터베이스에서 날짜 시간을 읽으면, UTC 대신 새로 설정한 시간대의 인식 날짜, 시간이 반환됨
    - `USE_TZ` 가 False인 상태로 이 값을 설정하는 것은 error가 발생하므로 주의
    - https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

- USE_I18N
    - Django의 번역 시스템을 활성화해야하는지 여부를 지정

- USE_L10N
    - 데이터의 지역화된 형식(localized formatting)을 기본적으로 활성화할지 여부를 지정
    - True일 경우, Django는 현재 locale의 형식을 사용하여 숫자와 날짜를 표시

- USE_TZ
    - datetimes가 기본적으로 시간대를 인식하는지 여부를 지정
    - True일 경우 Django는 내부적으로 시간대 인식 날짜, 시간을 사용
