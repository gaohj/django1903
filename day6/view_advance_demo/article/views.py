from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import Article,Student
from django.views.decorators.http import require_http_methods,require_GET,require_POST,require_safe
from django.db.models import F,Q,Count
# Create your views here.
#require_GET = @require_http_methods(['GET'])
#require_POST = @require_http_methods(['POST'])
@require_GET
def index(request):
    # Article.objects.bulk_create([
    #     Article(title="没有金刚钻别揽瓷器活1",content="海底月是天上月,眼前人是心上人1",price=12.342),
    #     Article(title="没有金刚钻别揽瓷器活2",content="海底月是天上月,眼前人是心上人2",price=12.341),
    #     Article(title="没有金刚钻别揽瓷器活3",content="海底月是天上月,眼前人是心上人3",price=12.343),
    #     Article(title="没有金刚钻别揽瓷器活4",content="海底月是天上月,眼前人是心上人4",price=12.344),
    # ])
    articles = Article.objects.all()

    # return HttpResponse('首页')
    return render(request,'index.html',context={"articles":articles})
@require_http_methods(['GET','POST'])
def add_article(request):
    #get方法让用户看到页面
    if request.method == 'GET':
        return render(request,'add_article.html')
    #post方法接收用户的提交
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        price = request.POST.get('price')
        Article.objects.create(title=title,content=content,price=price)
        return HttpResponse('success')

def index1(request):
    #http://www.baidu.com/?username=houxue@password=123456
    username = request.GET.get('username')
    if username:
        return HttpResponse("欢迎")
    else:
        return redirect(reverse('signin'))


def signin(request):
    return HttpResponse("登录页")

#WSGIRequest对象
def signup(request):
    #http://192.168.58.40:9000/signup/?username=kangbazi&password=123321
    # print(request.path) #打印路由地址signup/
    # print(request.get_full_path()) #/signup/?username=kangbazi&password=123321
    # print(request.get_raw_uri())#http://192.168.58.40:9000/signup/?username=kangbazi&password=123321
    # for key,value in request.META.items():
    #     print("%s:%s" %(key,value))
    # print(request.get_host())
    print(request.META['REMOTE_ADDR'])
    return HttpResponse("注册页")

def index6(request):
    #查询学过“黄老师”所教的“所有课”的同学的id、姓名；
    #1 每一位学生学习的老师所教课程的数量  A  Count  annotate nums=Count('score__course',filter=Q(score__course__teacher__name='黄老师'))
    #2 课程表中 老师教了哪些课程   B Course.objects.filter(teacher__name='黄老师').count()
    #3 如果 A 等于B 意味着 这个学生学习了老师的所有课程 如果不等表示
    #没有学完老师教的所有课程
    Student.objects.annotate(nums=Count('score__course',filter=Q(score__course__teacher__name='黄老师'))).filter(nums=Course.objects.filter(teacher__name='黄老师').count()).values('id','name')
    return HttpResponse('index6')