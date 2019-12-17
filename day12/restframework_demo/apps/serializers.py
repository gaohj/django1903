from rest_framework import serializers

from apps.models import Book,Game,Movie,User

class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ("url","book_name","book_price")

class Book1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("id","book_name","book_price")

class Book2Serializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    book_name = serializers.CharField()
    book_price = serializers.FloatField()

    #更新数据
    def update(self, instance, validated_data):
       instance.book_name = validated_data.get('book_name') or instance.book_name
       instance.book_price = validated_data.get('book_price') or instance.book_price
       instance.save()
       return instance


    #往里数据库中添加数据
    def create(self, validated_data):
       return Book.objects.create(**validated_data)


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ("id","game_name","game_price")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id","movie_name","movie_price")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","user_name","user_password")