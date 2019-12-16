from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .forms import RegisterForm,LoginForm,TransferForm
from .models import User
from .decorators import login_required
from django.db.models import F
# Create your views here.

def index(request):
    return render(request,'index.html')


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            username = form.cleaned_data.get('username')
            User.objects.create(username=username,password=password,email=email,balance=1000)
            return redirect(reverse('login'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('register'))



class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(password=password, email=email).first()
            if user:
                request.session['user_id'] = user.pk
                return redirect(reverse('index'))
            else:
                print("用户名或者密码错误")
                return redirect(reverse('login'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('login'))

from django.utils.decorators import method_decorator

@method_decorator(login_required,name='dispatch')
class TransferView(View):
    def get(self,request):
        return render(request, 'transfer.html')
    def post(self,request):
        form = TransferForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            money = form.cleaned_data.get('money')
            #获取当前登录用户
            user = request.front_user
            #用户的余额要大于转账的余额
            if user.balance >= money:
                # 对方余额 增加转账余额
                User.objects.filter(email=email).update(balance=F('balance')+money)
                # 当前用户 减少转账余额
                user.balance -=money #转出去的用户钱 减掉
                user.save()
                return HttpResponse("增加余额成功")
            else:

                return HttpResponse("余额不足")
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('transfer'))



def logout(request):
    request.session.flush()
    return redirect(reverse('index'))





