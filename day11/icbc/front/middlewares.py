#encoding:utf-8
from .models import User

def front_user_middleware(get_response):
    def middleware(request):
        response = ''
        return response

    return middleware
