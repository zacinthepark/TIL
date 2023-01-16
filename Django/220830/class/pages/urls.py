from django.urls import path
from pages import views

app_name = "pages"
# pages에 관련된 url만 남김
urlpatterns = [
    path('index/', views.index, name="index")
]
