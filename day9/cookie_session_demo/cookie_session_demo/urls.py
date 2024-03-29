"""cookie_session_demo URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/', views.delete_cookie,name='delete'),
    path('list/', views.get_cookie,name='list'),
    path('cms/', views.cms_cookie,name='cms'),
    path('session/', views.session_view,name='session'),
    path('get_session/', views.get_session,name='get_session'),
    path('del_session/', views.delete_session,name='del_session'),
]
