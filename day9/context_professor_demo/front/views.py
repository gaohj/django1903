from django.shortcuts import render
from .models import User
from django.http import HttpResponse
# Create your views here.

def index(request):
    users = []
    for x in range(100000,200000):
        user = User(username="用户:%s"%x,password="密码:%s" %x,telephone=1388888888)
        users.append(user)
    User.objects.bulk_create(users)
    return HttpResponse('创建用户成功')

def list(request):
    users = User.objects.filter(id__gte=10000).all()
    context = {
        'users':users
    }
    return render(request,'index.html',context=context)