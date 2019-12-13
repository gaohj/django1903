from django.shortcuts import render,redirect,reverse
from django.views.generic import View
from . models import User
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    if request.front_user:
        print(request.front_user.username)
    return render(request,'index.html')
class SigninView(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = User.objects.filter(username=username,password=password).first()
        if user:
            request.session['user_id'] = user.id
            return redirect(reverse('index'))
        else:
            messages.info(request,"用户名或者密码错误")
            return redirect(reverse('signin'))

