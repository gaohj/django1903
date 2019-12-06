from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
# Create your views here.

def index(request):
    # book =Book(name='水浒传',author='施耐庵',price=110)
    # book.save()

    #根据主键查询
    # book = Book.objects.get(pk=2)
    # print(book)
    # book = Book.objects.filter(name='水浒传').first()
    # print(book)

    #改
    # book = Book.objects.get(pk=2)
    # # book.name = '三国演义'
    # # book.author = '罗贯中'
    # # book.price = 200
    # # book.save()
    # print(book)

    #删除
    book = Book.objects.first()
    book.delete()
    return HttpResponse('首页')
