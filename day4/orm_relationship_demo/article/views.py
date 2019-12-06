from django.http import HttpResponse
from .models import Article,Category
from frontuser.models import FrontUser
# Create your views here.

def index(request):
    author = FrontUser(username='kangbazi')
    author.save()
    category = Category(name='国产')
    category.save()
    return HttpResponse('Index success')
def one_to_many(request):
    #一对多关联插入操作
    # article = Article(title='我要你',content='就不要脸了')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    # article.author = author
    # article.category = category
    # article.save()

    #查询操作
    # category = Category.objects.first()
    # articles = category.article_set.all()
    # for article in  articles:
    #     print(article)  #打印的是对象Article object (3)

    # category = Category.objects.first()
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)
    articles = Article.objects.first()
    articles.author.username = 'kangbazi666'
    print(articles.author.username)
    articles.save()
    return HttpResponse('success')

def delete_view(request):
    category = Category.objects.get(pk=2)
    category.delete()
    return HttpResponse('delete success')