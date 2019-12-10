from django.http import HttpResponse
from .models import Book,BookOrder,Publisher
from django.db import connection
from django.db.models import F,Q,Count,Prefetch
# Create your views here.
def index(request):
    print(type(Book.objects))
    return HttpResponse('首页')

def index2(request):
    #链式调用
    # books = Book.objects.filter(id__gte=1).exclude(id=3)
    # for book in books:
    #     print(book)
    # print(connection.queries)
    books = Book.objects.annotate(author_name=F("author__name"))
    for book in books:
        print("%s:%s" %(book.name,book.author_name))
    return HttpResponse('index2')


def index3(request):
    orders = BookOrder.objects.all()
    for order in orders:
        print("%s:%s:%s" %(order.id,order.create_time,order.price))
    return HttpResponse('index3')

def index4(request):
    # books = Book.objects.values("id","name",author_name=F("author__name"))
    # books = Book.objects.values("id","name",order_nums=Count("bookorder"))
    books = Book.objects.values_list('name')
    """
    ('三国演义',)
    """
    books = Book.objects.values_list('name',flat=True)
    """
    三国演义
    """
    for book in books:
        print(book)
    print(connection.queries[-1])
    return HttpResponse('index4')

def index5(request):
    books = Book.objects.all()
    for book in books:
        print(book.name)
    return HttpResponse('index5')

def index6(request):
    #原本 先查出 图书的详细信息  然后根据图书对应的作者的id 去作者表查询
    #再根据出版社id 去出版社中查询信息  12次查询
    #查出图书的同时 将作者出版社一并查出来 不需要每次再去查询一次了
    #也就是说下面只需要4次查询就够了
    books = Book.objects.select_related("author","publisher")
    for book in books:
        print(book.author.name)
        print(book.publisher.name)

    print(connection.queries[-1])
    return HttpResponse('index6')

def index7(request):
    # books = Book.objects.prefetch_related("bookorder_set")
    # for book in books:
    #     print("+"*50)
    #     print(book.name)
    #     orders = book.bookorder_set.all()
    #     for order in orders:
    #         print(order.id)
    #     #每一本书销售的订单id
    #     #select_related 支持 订单查询图书的信息 不能做到根据图书id查询出订单的信息
    #
    # books = Book.objects.prefetch_related("author")
    # for book in books:
    #     print(book.author.name)
    #查询图书销售的价格大于90的图书的订单  按照惯例 可以使用
    #filter(bookorder__price__gt>90) #查询次数多
    #为了减少关联的查询次数
    prefetch = Prefetch("bookorder_set",queryset=BookOrder.objects.filter(price__gte=90))
    books = Book.objects.prefetch_related(prefetch)
    for book in books:
        print("+"*50)
        print(book.name)
        orders = book.bookorder_set.all()
        for order in orders:
            print(order.id)
    print(connection.queries)
    return HttpResponse('index7')

def index8(request):
    #books = Book.objects.defer("name")  #不过滤主键id   排除name
    # books = Book.objects.only("name") #只要name 不排除id
    # books = Book.objects.defer("name")
    # for book in books:
    #     print("+"*50)
    #     print(book.name)
    books = Book.objects.get(pk=2)
    print(books)
    print(connection.queries)
    return HttpResponse('index8')

def index9(request):
    # books = Publisher.objects.create(name="666出版社") #创建一条
    books = Publisher.objects.bulk_create([
        Publisher(name="123"),
        Publisher(name="456"),
        Publisher(name="789"),
    ])
    print(connection.queries)
    return HttpResponse('index9')

def index10(request):
    # count = Book.objects.count()
    # print(count)
    # result = Book.objects.filter(name='三国演义').exists()
    # print(type(result))
    result = Book.objects.filter(bookorder__price__gte=80).order_by("bookorder__price").distinct()
    for res in result:
        print("%s" %(res.name))
    print(connection.queries)
    return HttpResponse('index10')

def index11(request):
    books = Book.objects.all()[1:]
    for book in books:
        print(book.name)
    print(connection.queries)
    return HttpResponse('index11')

def index12(request):
    books = Book.objects.all()
    print(connection.queries)
    return HttpResponse('index12')