from django.shortcuts import render,redirect,reverse
from django.db import connection
# Create your views here.
def get_cursor():
    return connection.cursor()

def index(request):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book")
    books = cursor.fetchall()
    context = {
        'books':books
    }
    return render(request,'index.html',context=context)

def add_book(request):
    print(request.method)
    if request.method == 'GET': #判断如果是get请求 那么查看页面
        return render(request,'add.html')
    else:
        name = request.POST.get('name')
        author = request.POST.get('author')
        # print(name,author)
        cursor = get_cursor()
        cursor.execute("insert into book(id,name,author) values (null,'%s','%s')" %(name,author))
        return redirect(reverse('index'))