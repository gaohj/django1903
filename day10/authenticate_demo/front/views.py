from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from .models import Person
# Create your views here.
#12345678910111213
from front.models import User
#看看你有多长间时找出错误
def index(request):
    # user = User.objects.create_user(username='kangbazi',password='123456',email='chengcheng')
    # user = User.objects.create_user(username='pengpeng',password='123456',email='xiaoqin')
    # user = User.objects.create_superuser(username='chengcheng',password='123456',email='xinxin')
    # user.last_name = 'qinqin'
    # user.first_name = 'xiuxiu'
    # user.save()
    # user = User.objects.get(pk=1)
    # user.is_active =False
    # user.set_password('654321')
    # user.save()
    # user = authenticate(username='chengcheng',password='123456')
    # if user:
    #     print("%s 登录成功" % user.username)
    # else:
    #     print("用户名或者密码错误")
    return HttpResponse('success')

# def proxy_view(request):
#     black_list = Person.get_blacklist()
#     for person in black_list:
#         print(person.username)
#     return HttpResponse('获取成功')

# def my_authenticate(telephone,password):
#     user = User.objects.filter(extension__telephone=telephone).first()
#     if user:
#         is_correct = user.check_password(password) #检查密码是否正确
#         if is_correct:
#             return user
#         else:
#             return None
#     else:
#         return None

# def one_view(request):
#     # user = User.objects.create_user(username='xiaocheng1',email='xiaochenggushi@163.com',password='123456123')
#     # user.extension.telephone = 13888888889
#     # user.extension.school = '北大'
#     # user.save()
#     telephone = request.GET.get('telephone')
#     password = request.GET.get('password')
#     user  = my_authenticate(telephone,password)
#     if user:
#         print("验证成功 %s" % user.username)
#     else:
#         print("验证失败")
#     return HttpResponse('一对一扩展模型')

def inherite_view(request):
    telephone = '18777717777'
    username = 'xinxinrongrong1'
    password = '1234567'
    email = 'xinxin1@126.com'
    user = User.objects.create_user(telephone=telephone,username=username,password=password,email=email)
    print(user.username)

    user = authenticate(request,username='18777717777',password='1234567')
    if user:
        print("验证成功")
        print(user.username)
    else:
        print("验证失败")
    return HttpResponse('AbstractUser扩展模型')