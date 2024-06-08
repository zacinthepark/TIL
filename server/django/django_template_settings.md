## Template Settings

---

- https://docs.djangoproject.com/en/4.2/ref/templates/api/

```python
# mysite/settings.py
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates", 
        "DIRS": [BASE_DIR / 'templates'], 
        "APP_DIRS": True, 
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug", 
                "django.template.context_processors.request", 
                "django.contrib.auth.context_processors.auth", 
                "django.contrib.messages.context_processors.messages"
            ]
        }
    }
]

```

- 앱 디렉토리 로더
    - `django.template.loaders.app_directories.Loader`
    - `INSTALLED_APPS`에 작성한 app 순서로 `appName/templates/` 경로에서 검색
        - 그러므로 템플릿 폴더의 이름은 반드시 templates로 지정

- 파일 디렉토리 로더
    - `django.template.loaders.filesystem.Loader`
    - `TEMPLATES`에 있는 `DIRS` 경로에서 파일을 검색
    - 템플릿 파일을 찾을 때 여기도 찾아달라고 명령하는 것

- 샌드위치 구조
    - `appName/templates/appName/`
    - 등록된 앱들 중 같은 이름의 템플릿이 있을 경우 앱 순서에 따라 먼저 등록된 것을 렌더링함
    - 이를 방지하기 위해 templates 폴더 아래 하위 디렉토리 경로를 하나 더 추가하여 물리적인 이름 공간을 만듬
    - `render(request, 'articles/index.html')`, `redner(request, 'pages/index.html')`과 같이 접근
