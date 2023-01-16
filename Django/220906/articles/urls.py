from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    # path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),           # GET / POST (new 페이지 렌더링, 새로운 데이터 생성을 분기를 통해 둘 다 처리)
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),  # GET / POST (edit 페이지 렌더링, 기존 데이터 수정을 분기를 통해 둘 다 처리)
]
