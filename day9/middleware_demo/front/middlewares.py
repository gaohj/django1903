from .models import User

def front_user_middleware(get_response): #get_response是一个方法
    #执行一些初始化的代码
    print("在这里我先执行一些初始化的代码")
    def middleware(request): #真正执行是在这里
        print("这个位置执行的是request到达view之前的代码")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
                #将登录用户的详细信息 绑定到request对象上
            except:
                request.front_user = None
        else:
            request.front_user = None

        #上面执行的代码就是request到达view之前执行的
        response = get_response(request) #request对象上面有登录用户的详细信息
        print("以这个为界限它后边就是response到达浏览器之前执行的代码")
        return response
    return middleware

class FrontUserMiddleWare(object):
    def __init__(self,get_response):
        #在这里执行一些初始化的代码
        print("在这里执行一些初始化的代码")
        self.get_response = get_response
    def __call__(self,request):#为每个请求响应执行的代码
        print("这里执行的是request到达view之前的代码")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
                # 将登录用户的详细信息 绑定到request对象上
            except:
                request.front_user = None
        else:
            request.front_user = None

        #上面就是request到达view之前的代码
        response = self.get_response(request) #这是界限
        #下面就是resonse到达浏览器之前执行的代码
        print("下面就是resonse到达浏览器之前执行的代码 788888")
        return response
from django.utils.deprecation import MiddlewareMixin
class FrontUserMiddleWareMixin(MiddlewareMixin):
    def __init__(self,get_response):
        #在这里执行一些初始化的代码
        print("在这里执行一些初始化的代码")
        super(FrontUserMiddleWareMixin, self).__init__(get_response)


    #request到达view之前
    def process_request(self,request):
        print("这里执行的是request到达view之前的代码")
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
                # 将登录用户的详细信息 绑定到request对象上
            except:
                request.front_user = None
        else:
            request.front_user = None

    #responsed到达浏览器
    def process_response(self,request,response):
        print("resonse到达浏览器之前执行的代码99999")
        return response
