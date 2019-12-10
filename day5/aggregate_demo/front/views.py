from django.http import HttpResponse
from .models import Book,BookOrder,Publisher,Author
from django.db.models import Avg,Sum,Count,Max,Min,F,Q
from django.db import connection
# Create your views here.
def index(request):
    #获取所有图书的平均价格
    # result = Book.objects.aggregate(Avg("price"))
    result = Book.objects.aggregate(avg=Avg("price"))
    #这里的avg 类似于 select count(*) as allofnum   allofnum就是别名
    #也是最终显示出来的 名字
    print(result)
    # print(result.query) filter中可以是用这种方式查看最终执行的sql语句
    #aggregate 不能这么用 必须通过以下方式
    print(connection.queries)
    return HttpResponse('index')

def index1(request):
    #每一本数销售的平均价格
    """
    三国演义:89.33333333333333
    水浒传:93.5
    西游记:None
    红楼梦:None

    :param request:
    :return:
    """
    result = Book.objects.aggregate(avg=Avg('bookorder__price'))
    print(result)
    print(connection.queries)
    print("="*60)
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print('%s:%s'% (book.name,book.avg))
    print(connection.queries)
    return HttpResponse('index1')

def index2(request):
    #book表总共有多少本 aggregate
    #每一本书  annotate


    book = Book.objects.aggregate(book_nums=Count('id'))
    print(book)
    print(connection.queries)

    #作者表中不同的邮箱
    result = Author.objects.aggregate(email_nums=Count('email',distinct=True))
    print(result)
    print(connection.queries)

    #每一本图书的销量
    books = Book.objects.annotate(book_num=Count("bookorder__id"))
    for book in books:
        print('%s:%s' % (book.name, book.book_num))
    print(connection.queries)
    return HttpResponse('index2')

def index3(request):
    #作者的最大年龄和最小年龄
    result = Author.objects.aggregate(max=Max('age'),min=Min('age'))
    print(result)
    print(connection.queries)
    print("=" * 60)

    #每一本图书 售卖的时候最大价格和最小价格
    books = Book.objects.annotate(max=Max("bookorder__price"),min=Min("bookorder__price"))
    for book in books:
        print('%s:%s:%s' % (book.name, book.max,book.min))
    print(connection.queries)
    return HttpResponse('index3')


def index4(request):
    #所有图书的销售总额
    result = BookOrder.objects.aggregate(sums=Sum('price'))
    print(result)
    print(connection.queries)
    print("=" * 60)
    #每一本图书的销售总额
    #西游记卖了三本 总价 三国演义两本 总价
    books = Book.objects.annotate(total=Sum("bookorder__price"))
    for book in books:
        print('%s:%s' % (book.name, book.total))
    print(connection.queries)
    return HttpResponse('index4')

def index5(request):
    #2018年度销售的总额
    result = BookOrder.objects.filter(create_time__year=2018).aggregate(total=Sum('price'))
    print(result)
    print(connection.queries)
    print("=" * 60)

    #每一本图书在2019年度的销售总额
    books = Book.objects.filter(bookorder__create_time__year=2019).annotate(total=Sum("bookorder__price"))
    for book in books:
        print('%s:%s' % (book.name, book.total))
    print(connection.queries)
    return HttpResponse('index5')

def index6(request):
    # Book.objects.update(price=F("price")+100)
    # print(connection.queries[-1])
    authors = Author.objects.filter(name=F("email"))
    for author in authors:
        print("%s:%s"%(author.name,author.email))
    return HttpResponse('index6')

def index7(request):
    #价格大于100 并且评分高于4.8的图书
    # books = Book.objects.filter(price__gt=100,rating__gte=4.8)
    # books = Book.objects.filter(Q(price__gte=100)&Q(rating__gte=4.8))
    # 价格小于100 或者  评分小于4.8的
    books = Book.objects.filter(Q(price__lt=100) | Q(rating__lt=4.8))

    #价格大于100  并且 图书名字不包含传的
    books = Book.objects.filter(Q(price__lt=100) & ~Q(name__icontains='传'))
    for book in books:
        print("%s:%s:%s" % (book.name,book.price,book.rating))
    return HttpResponse('index7')
