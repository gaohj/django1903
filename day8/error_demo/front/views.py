from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
# Create your views here.


def index(request):
    #http://127.0.0.1:9000/?username=daokexiong
    username = request.GET.get('username')
    if username:
        return HttpResponse('首页')
    else:
        return redirect(reverse('errors:403'))