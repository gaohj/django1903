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

#第一种分页
# class ArticleListView(ListView):
#     model = Article
#     template_name = 'article_list1.html'
#     context_object_name = 'articles'
#     paginate_by = 10
#     ordering = 'create_time'
#     page_kwarg = 'p'
#
#     def get_context_data(self,**kwargs):
#         context = super(ArticleListView, self).get_context_data()
#         paginator = context.get('paginator')
#         page_obj = context.get('page_obj')
#         return context
    #如果你不想要全部数据 只要部分数据 那么 需要重写
    #get_queryset方法
    # def get_queryset(self):
    #     return Article.objects.filter(id__lte=100)

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
        pagination_data = self.get_pagination_data(paginator,page_obj)
        context.update(pagination_data)
        return context

    #知道你左边的页码是多少
    #右边的页码是多少
    #左边是否还有更多页码  #总共10 页  当前第4页 左边没有更多页码了
    #右边是否还有更多页码
    #需要知道当前的页码是多少
    def get_pagination_data(self,paginator,page_obj,arrount_count=2):
        current_page = page_obj.number  #当前页
        number_pages = paginator.num_pages #总共多少页

        left_has_more = False  #标志位 默认左边没有更多
        right_has_more = False  #标志位 默认右边没有更多

        if current_page <= arrount_count + 2:  # 如果当前页码小于等于4
            left_pages = range(1,current_page)  #那么左边页码就显示 1 2 3
        else:
            left_has_more = True   #当前第10页 左边应该显示 89 就是range(8,10)
            left_pages = range(current_page-arrount_count,current_page)

        if current_page >= number_pages-arrount_count-1:
            # 总共40页为例如果当前页码大于等于
            #如果大于等于37页就不能显示省略号了而是显示所有的页码
            right_pages = range(current_page+1,number_pages+1)
            #37 右边应该显示 38 39 40  range(38,41)
        else:
            right_has_more = True   #当前第10页 左边应该显示 89 就是range(8,10)

            right_pages = range(current_page+1,current_page+arrount_count+1) #如果第10页
            #右边应该是 11 12   range(11,13)


        return {
            'left_has_more':left_has_more,
            'right_has_more':right_has_more,
            'left_pages':left_pages,
            'right_pages':right_pages,
            'number_pages':number_pages,
            'current_page':current_page
        }


