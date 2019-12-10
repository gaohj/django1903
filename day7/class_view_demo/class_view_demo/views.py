from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View,TemplateView


class BookListView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'index.html')
class AddBookView(View):
    #自动判断请求方式 为get 查看添加页面
    def get(self,request,*args,**kwargs):
        return render(request,'add_book.html')
    #自动判断请求方式为post 接收前段用户提交的数据
    def post(self,request,*args,**kwargs):
        book_name = request.POST.get('name')
        book_author = request.POST.get('author')
        print("name:{},author:{}".format(book_name,book_author))
        return HttpResponse("success")

class BookDetailView(View):
    def get(self,request,book_id):
        return HttpResponse('图书的id是:%s' % book_id)

    #如果请求方式不被允许  那么走这里
    def http_method_not_allowed(self, request, *args, **kwargs):
        return HttpResponse("不好意思不支持get以外其它的请求")

    # 不管请求方式是什么 都会走这里
    def dispatch(self, request, *args, **kwargs):
        print("虽然你只支持get请求但是所有请求方法我都会相应一下")
        return super(BookDetailView, self).dispatch(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        context = {
            'phone':'13888888888'
        }
        return context