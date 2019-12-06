from django.http import HttpResponse
from .models import Article,Category
from datetime import datetime
from django.utils.timezone import make_aware
# Create your views here.

def index(request):
    category = Category(name='南亚')
    category.save()
    article = Article(title='泰国变性',content='变性人寿命真的很低')
    article.category = category
    article.save()
    return HttpResponse('首页')

def index1(request):
    # article = Article.objects.filter(title__exact='抗日战争')
    article = Article.objects.filter(title__iexact='抗日战争')
    print(article.query)
    print(article)
    return HttpResponse('index1')

def index2(request):
    # article = Article.objects.filter(title__icontains='抗日')
    article = Article.objects.filter(title__contains='抗日')
    print(article.query)
    print(article)
    return HttpResponse('index2')

def index3(request):
    # articles = Article.objects.filter(id__in=[1,2,3])
    # # print(article.query)
    # # print(article)
    # for article in articles:
    #     print(article)
    # categories = Category.objects.filter(articles__in=[1,2,3])
    # for category in categories:
    #     print(category)
    #标题中有抗日的所有的文章的分类
    article = Article.objects.filter(title__icontains='抗日')
    categories = Category.objects.filter(articles__in=article)
    for category in categories:
        print(category)
    print(categories.query)
    return HttpResponse('index3')


def index4(request):
    article = Article.objects.filter(category_id__gte=1)
    print(article.query)
    print(article)
    return HttpResponse('index4')

def index5(request):
    # article = Article.objects.filter(title__istartswith='抗日')
    article = Article.objects.filter(title__endswith='战争')
    print(article.query)
    print(article)
    return HttpResponse('index5')

def index6(request):
    start_time = make_aware(datetime(year=2019,month=9,day=6,hour=18,minute=16,second=18))
    end_time = make_aware(datetime(year=2019,month=12,day=6,hour=18,minute=16,second=18))
    article = Article.objects.filter(create_time__range=(start_time,end_time))
    print(article.query)
    print(article)
    # article = Article.objects.all()
    # print(article)
    return HttpResponse('index6')

def index7(request):
    article = Article.objects.filter(title__iregex=r'^h')
    print(article.query)
    print(article)
    return HttpResponse('index7')