from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
#http://192.168.58.40;9000/?username=zpc
def index(request):
    #接收参数的值
    username = request.GET.get('username')
    if username:
        return HttpResponse('<h1>后台cms首页</h1>')
    else:
        # # return redirect('/login/')
        # login_url = reverse('cms:login')
        # print("*"*30)
        # print(login_url)
        # print("*"*30)
        #获取当前实例
        current_namespace = request.resolver_match.namespace
        return redirect(reverse('%s:login'%current_namespace))
        # return redirect(login_url)
def login(request):
    return  HttpResponse('后台登录页')