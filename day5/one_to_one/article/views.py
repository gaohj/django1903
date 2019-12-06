from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Tag,Category
from frontuser.models import FrontUser,UserExtension
# Create your views here.
def index(request):
    # user = FrontUser(username='鹏鹏')
    # user.save()
    # category = Category(name='日韩系列')
    # category.save()
    # article = Article(title='为什么我的眼睛如此亮',content='因为眼睛里全是你 你的名字')
    # article.category = category
    # article.author = user
    # article.save()
    #查询发表了我要在你身上做春天对樱桃做的事情 这篇文章的作者信息
    #如果加了 related_query_name='art'
    # user = FrontUser.objects.filter(art__title='我要在你身上做春天对樱桃做的事情')
    # print(user)
    user = FrontUser.objects.get(pk=3)
    print(user.article.all()) #这里不能用 art 还是只能用article
    return HttpResponse('首页')

def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school='清华')
    # extension.user = user
    # extension.save()
    #学校是谁的学校
    extension = UserExtension.objects.first()
    print(extension.user)
    user = FrontUser.objects.first()
    print(user.extension)



    return HttpResponse('one_to_one_view success')

def many_to_many_view(request):
    # article = Article.objects.get(pk=2)
    # tag = Tag.objects.get(pk=5)
    # tag.articles.add(article)
    # article.tag_set.add(tag)
    # tag.article_set.add(article)
    # article.tags.add(tag)
    # tag = Tag.objects.get(pk=4)
    # articles = tag.tags.all()
    # print(articles)
    # for article in  articles:
    #     print(article)
    article = Article.objects.get(pk=2)
    tags = article.tags.all()
    print(tags)
    for tag in tags:
        print(tag)
    return HttpResponse('many_to_many_view success')