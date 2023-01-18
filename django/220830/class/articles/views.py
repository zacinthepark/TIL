from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple', 'orange', 'banana']
    info = {'name': 'JIN'}
    context = {
        'foods': foods,
        'info': info,
    }
    return render(request, 'articles/greeting.html', context)

def dinner(request):
    foods = ['pizza', 'spaghetti', 'chinese noodle']
    pick = random.choice(foods)
    info = {'name': 'JIN'}
    context = {
        'foods': foods,
        'pick': pick,
        'info': info,
    }
    return render(request, 'articles/dinner.html', context)

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    data = request.GET.get('message')
    context = {
        'data': data
    }
    return render(request, 'articles/catch.html', context)

def fake_google(request):
    return render(request, 'articles/fake-google.html')

# urls.py에서 던지는 name을 파라미터로 받아야 함
def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)