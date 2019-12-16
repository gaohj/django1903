#encoding:utf-8
from .models import User

def front_user_middleware(get_response):
    def middleware(request):
        # 初始化的代码
        print("开始初始化")
        #request到达view的代码
        user_id = request.session.get('user_id')
        if user_id:
            try:
                user = User.objects.get(pk=user_id)
                request.front_user = user
            except:
                request.front_user = None
        else:
            request.front_user = None
        response = get_response(request)
        #response到达浏览器的代码

        return response

    return middleware
