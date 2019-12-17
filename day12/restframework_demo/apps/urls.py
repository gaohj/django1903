from django.urls import path
from rest_framework import routers

from apps import views

router = routers.DefaultRouter() #实例化一个路由对象

router.register(r'books',views.BookView)