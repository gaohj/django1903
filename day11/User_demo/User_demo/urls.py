"""User_demo URL Configuration

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
from front import views

urlpatterns = [
    path('', views.index,name='index'),
    path('inherit/', views.inherit_view,name='inherit'),
    path('login/', views.my_login,name='login'),
    path('logout/', views.my_logout,name='logout'),
    path('profile/', views.profile_demo,name='profile'),
    path('profiles/', views.profiles,name='profiles'),
    path('add_article/', views.add_article,name='add_article'),
    path('add_permission/', views.add_permission,name='add_permission'),
    path('operate_permission/', views.operate_permission,name='operate_permission'),
    path('operate_group/', views.operate_group,name='operate_group'),

]
