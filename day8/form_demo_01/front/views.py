from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import User
from .forms import MessageBoardForm,MyForm,RegisterForm
# Create your views here.

class IndexView(View):
    #将表单映射到模板上
    def get(self,request):
        form = MessageBoardForm()
        return render(request,'index.html',context={"form":form})
    def post(selfr,request):
        form = MessageBoardForm(request.POST)
        #查看输入是否符合要求
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print("="*60)
            print(title)
            print(content)
            print(email)
            print(reply)
            print("="*60)
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

class MyView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        form  = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            price = form.cleaned_data.get('price')
            personal_website = form.cleaned_data.get('personal_website')
            telephone = form.cleaned_data.get('telephone')
            print(email,price,personal_website,telephone)
            return HttpResponse('OK')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

class SignupView(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        form  = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            telephone = form.cleaned_data.get('telephone')
            password1 = form.cleaned_data.get('password1')
            User.objects.create(username=username,password=password1,telephone=telephone)
            return HttpResponse('OK')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')