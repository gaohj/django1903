from django.shortcuts import render
from django.http import HttpResponse
from .models import Article,Tag,Category
from frontuser.models import FrontUser,UserExtension
# Create your views here.
def index(request):
    user = FrontUser(username='鹏鹏')
    user.save()
    category = Category(name='日韩系列')
    category.save()
    article = Article(title='为什么我的眼睛如此亮',content='因为眼睛里全是你 你的名字')
    article.category = category
    article.author = user
    article.save()
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
    article = Article.objects.get(pk=2)
    tag = Tag(name='国产系列')
    tag.save()
    # tag.articles.add(article)
    # article.tag_set.add(tag)
    # tag.article_set.add(article)
    article.tags.add(tag)
    return HttpResponse('many_to_many_view success')