#encoding:utf-8
from django.http import HttpResponse
from datetime import datetime
from django.utils.timezone import make_aware
#设置cookie 是response对象
def index(request):
    response = HttpResponse('index') #先要构建一个response对象
    expires = datetime(year=2019,month=12,day=12,hour=20,minute=30,second=30)
    expires = make_aware(expires)
    response.set_cookie('user_id','chengcheng',expires=expires,max_age=3600,path='/cms/')
    return response
#获取cookie信息 需要通过request对象
def get_cookie(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

def cms_cookie(request):
    cookies = request.COOKIES
    username = cookies.get('user_id')
    return HttpResponse(username)

#删除cookie也是response对象
def delete_cookie(request):
    response = HttpResponse('delete')
    response.delete_cookie('user_id')
    return response
from datetime import timedelta
def session_view(request):
    # expires = datetime(year=2019, month=12, day=12, hour=20, minute=30, second=30)
    # expires = make_aware(expires)
    request.session['username'] = 'chengcheng999999999999999'
    # expires = timedelta(100)
    # request.session.set_expiry(expires)
    return HttpResponse('session_view')

def get_session(request):
    username = request.session.get('username')
    print(username)
    return HttpResponse('获取session成功')
