from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import User,Article
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import ContentType,Permission,Group
from .forms import LoginForm

# Create your views here.
def inherit_view(request):
    user = User.objects.create_user(telephone='18888888886',username='chengcheng1',password='123321',email='cheng1@163.com')
    # user = authenticate(request,username='18777777777',password='123321')
    # if user:
    #     print(user.username)
    #     print('验证成功')
    # else:
    #     print("验证失败")
    return HttpResponse('创建成功')

#  重写了user模型  写登录方法 切记不能使用login作为方法名
#   因为  django 封装的名称 也叫 login
def my_login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            telephone = form.cleaned_data.get('telephone')
            print(telephone)
            password = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = authenticate(request,username=telephone,password=password)
            if user and user.is_active:
                login(request,user)
                if remember:
                    #如果用户勾选了记住我 表示使用全局的过期时间
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)

                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return HttpResponse('登录成功')
            else:
                return HttpResponse('用户名或者密码错误')
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))

def my_logout(request):
    logout(request)
    return HttpResponse('退出登录成功')
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def profile_demo(request):
    return HttpResponse("个人中心")


def add_permission(request):
    # 因为django 在权限是针对 模型级别
    # 获取模型对应的content_type  id
    content_type = ContentType.objects.get_for_model(Article)
    print(content_type)
    #接下来在权限表中添加权限即可
    permission = Permission.objects.create(codename="black_aritle",name="拉黑文章",content_type=content_type)
    return HttpResponse("添加权限成功")
