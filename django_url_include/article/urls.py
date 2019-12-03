from django.urls import re_path
from . import views

urlpatterns = [
    #r代表原生字符串
    re_path(r'^$',views.article),
    # path('list/<year>')
    re_path(r'^list/(?P<year>\d{4})/$',views.article_list),
    re_path(r'^list/(?P<month>\d{2})/$',views.article_list_month),
]