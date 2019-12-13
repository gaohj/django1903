from django.shortcuts import render,redirect,reverse
from .models import User
from django.views.generic import View
from .forms import SignUpForm,SignInForm
from django.contrib import messages
# Create your views here.
def index(request):
    users = User.objects.all()
    context = {
        'users':users
    }
    return render(request,'index.html',context=context)

class SignupView(View):
    def get(self,request):
        return render(request,'signup.html')

    def post(self,request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signup'))

class SigninView(View):
    def get(self,request):
        return render(request,'signin.html')

    def post(self,request):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #查询该用户名和密码的记录
            user = User.objects.filter(username=username,password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print('用户名或者密码错误')
                messages.info(request,'用户名或者密码错误')
                return redirect(reverse('signin'))
        else:
            errors = form.get_errors()
            for error in  errors:
               messages.info(request,error)
            return redirect(reverse('signin'))
def logout(request):
    request.session.flush()
    return redirect(reverse('index'))

def blog(request):
    return render(request,'blog.html')