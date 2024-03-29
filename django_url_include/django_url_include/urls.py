"""django_url_include URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from movie import views
#http://ip:端口号/book/5/
#http://ip:端口号/movie/50/
urlpatterns = [
    path('book/',include('book.urls')),
    # path('movie/',include('movie.urls')),
    path('movie/',include([
        path('',views.movie),
        path('detail/<int:movie_id>/',views.movie_detail),
        path('list/',views.movie_list),
    ])),
    path('article/',include('article.urls'))
]
