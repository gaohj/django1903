from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.contrib.auth import authenticate
# Create your views here.
def inherit_view(request):
    # user = User.objects.create_user(telephone='18777777777',username='chengcheng',password='123321')
    user = authenticate(request,username='18777777777',password='123321')
    if user:
        print(user.username)
        print('验证成功')
    else:
        print("验证失败")
    return HttpResponse('创建成功')