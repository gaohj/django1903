from django.shortcuts import render
from django.http import HttpResponse
from apps.models import Book,Game,Movie,User
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.exceptions import APIException,NotFound
from apps.serializers import Book2Serializer,GameSerializer,MovieSerializer,UserSerializer
from apps.authentications import UserAuthentication
from apps.permissions import UserLoginPermission
# Create your views here.
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = Book2Serializer

# class GameCreateApiView(CreateAPIView): #只能post请求
#class GameCreateApiView(ListAPIView): #只允许get请求
class GameCreateApiView(ListCreateAPIView): #GET 和POST 请求
    queryset = Game.objects.all()
    serializer_class = GameSerializer

#以上CBV限定请求的方式
# 接下来 我们尝试在 url中 限定请求方式
class MovieView(viewsets.ModelViewSet): #默认支持所有请求方式
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = UserAuthentication,
    permission_classes = UserLoginPermission,

from django.core.cache import cache
class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        action = request.query_params.get('action') #获取url中的参数
        if action == 'register':
            return self.create(request, *args, **kwargs)
        elif action == 'login':
            return self.do_login(request, *args, **kwargs)
        else:
            raise APIException("请提供正确的动作")


    def do_login(self,request, *args, **kwargs):
        user_name = request.POST.get('user_name')
        user_password = request.POST.get('user_password')
        try:
            user = User.objects.filter(user_name=user_name).first()
        except User.DoesNotExist as e:
            raise NotFound(detail="该用户不存在")
        if user.user_password != user_password:
            raise APIException(detail="用户密码错误")
        import uuid
        token = uuid.uuid4().hex

        cache.set(token,user.id,timeout=60*60*24*3)

        data = {
            'status':status.HTTP_200_OK,
            'msg':"登录成功",
            "token":token
        }

        return Response(data)

