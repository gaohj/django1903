#encoding:utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add_article,name='add_article'),
    path('list/',views.ArticleListView.as_view(),name='list'),
]