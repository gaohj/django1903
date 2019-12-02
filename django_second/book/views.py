from django.http import HttpResponse,HttpRequest

# Create your views here.
def book(request):
    #request接收前端用户所有的请求
    return HttpResponse("图书首页")

def book_detail(request,book_id,category_id):
    text = "您想要查看的文章id为%s,图书分类是:%s" % (book_id,category_id)
    return HttpResponse(text)

def author_detail(request):
    #http://ip:端口号/?id=100
    author_id = request.GET['id']
    text = "作者的id是:%s" % author_id
    return HttpResponse(text)