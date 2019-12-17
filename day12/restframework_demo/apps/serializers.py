from rest_framework import serializers

from apps.models import Book,Game,Movie,User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("url","book_name","book_price")