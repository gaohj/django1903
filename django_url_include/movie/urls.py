from django.urls import path
from . import views
urlpatterns = [
    path('',views.movie),
    path('detail/<int:movie_id>/',views.movie_detail),
    path('list/',views.movie_list),
]