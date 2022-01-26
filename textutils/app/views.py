from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index. <h1><a href='/home'>forword</a></h1>")
def home(request):
    return HttpResponse('''<h1>hello, <a href="https://docs.djangoproject.com/en/4.0/intro/tutorial01/">link django docs
    </a> <a href='/'>back</a> </h1>''')
def login(request):
    params={'name':'Anjan prasad','job':'Web developer'}
    return render(request, 'index.html',params)
def removepunc(request):
    maths =int(request.POST.get('maths','default'))
    science =int( request.POST.get('science','default'))
    social =int( request.POST.get('social','default'))
    total = maths+science+social
    percent=float(total/3)
    print(percent)
    json = {'total':total,'percentage':percent}
    return render(request,'percent.html',json)
def form(request):
    return render(request, 'form.html')