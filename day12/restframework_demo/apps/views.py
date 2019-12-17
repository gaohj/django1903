from django.shortcuts import render
from apps.models import Book,Game,Movie,User
from rest_framework import viewsets
from apps.serializers import BookSerializer
# Create your views here.
class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

