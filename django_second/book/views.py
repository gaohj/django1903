from django.http import HttpResponse,HttpRequest

# Create your views here.
def book(request):
    #request接收前端用户所有的请求
    return HttpResponse("图书首页")

def book_detail(request,book_id,category_id):
    text = "您想要查看的文章id为%s,图书分类是:%s" % (book_id,category_id)
    return HttpResponse(text)
