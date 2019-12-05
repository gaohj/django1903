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

def book_detail(request,book_id):
    cursor = get_cursor()
    cursor.execute("select id,name,author from book where id=%s" % book_id)
    book = cursor.fetchone()
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context=context)

def book_delete(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute("delete from book where id=%s" % book_id)
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除方法有误")