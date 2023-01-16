from django.urls import path
from articles import views

app_name = "articles"
# articles의 view에 관련된 url만 남김
urlpatterns = [
    path('index/', views.index, name="index"),
    path('greeting/', views.greeting, name ="greeting"),
    path('dinner/', views.dinner, name="dinner"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('fake-google/', views.fake_google, name="fake_google"),
    path('hello/<str:name>/', views.hello, name="hello"),
]
