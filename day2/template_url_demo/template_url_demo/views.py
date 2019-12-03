from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def login(request):
    #http://127.0.0.1:9000/?next=index
    #登录完成以后你应该跳到哪里
    next = request.GET.get('next')
    text = '登录完成以后跳转的url是:%s' % next
    return HttpResponse(text)

def book(request):
    return HttpResponse("图书页面")

def book_detail(request,book_id,category_id):
    text = '您的图书id是:%s,图书分类是:%s' %(book_id,category_id)

    return HttpResponse(text)

def movie(request):
    return HttpResponse("电影页面")

def city(request):
    return HttpResponse("同城页面")