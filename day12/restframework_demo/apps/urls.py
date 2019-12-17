from django.urls import path
from django.conf.urls import url
from rest_framework import routers

from apps import views

router = routers.DefaultRouter() #实例化一个路由对象

router.register(r'books',views.BookView)

urlpatterns = [
    path('games/',views.GameCreateApiView.as_view(),name='game'),
    url(r'^movies/$',views.MovieView.as_view(
        actions={
            'get': 'list',
            'post':'create'
        }
    )),
    url(r'^movies/(?P<pk>\d+)/',views.MovieView.as_view(
        actions={
            'get':'retrieve',
            'put':'update',
            'patch':'partial_update',
            'delete':'destroy',
        }
    )),
    url(r'^users/',views.UserCreateApiView.as_view(),name='users')

]