from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from django.views.generic import View,TemplateView,ListView
# Create your views here.
def add_article(request):
    articles = []
    for x in range(200):
        article = Article(title='标题：%s' % x,content='内容:%s' % x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse('成功')

class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_time'
    page_kwarg = 'p'

    def get_context_data(self,**kwargs):
        context = super(ArticleListView, self).get_context_data()
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        # pagination_data = self.get_pagination_data(paginator,page_obj)
        # context.update(pagination_data) #更新字典内容
        return context

    # def get_pagination_data(self,paginator,page_obj):
    #     current_page = page_obj.number #当前页码
    #     num_pages = paginator.num_pages #总共多少页面
    #
    #     return {
    #         'current_page':current_page,
    #         'num_pages':num_pages
    #     }

    #如果你不想要全部数据 只要部分数据 那么 需要重写
    #get_queryset方法
    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=100)
