#encoding:utf-8

from django.urls import path
from . import views
urlpatterns = [
    path('',views.book),
    # path('detail/<uuid:book_id>/',views.book_detail),
    # path('detail/<int:book_id>/',views.book_detail),
    # path('detail/<uuid:book_id>/',views.book_detail),
    # path('detail/<path:book_id>/',views.book_detail),
    path('detail/<book_id>/',views.book_detail),
    path('list/',views.book_list),
]