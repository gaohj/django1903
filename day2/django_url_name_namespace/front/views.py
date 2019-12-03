from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
#http://192.168.58.40;9000/?username=zpc
def index(request):
    #接收参数的值
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        # return redirect('/login/')
        login_url = reverse('front:login')
        print("*"*30)
        print(login_url)
        print("*"*30)
        return redirect(login_url)
def login(request):
    return  HttpResponse('前台登录页')