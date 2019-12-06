from django.db import models

# Create your models here.
#将一个类 变成可以映射到数据库中的模型
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,null=False,db_column='username')
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(null=False,default=0)

class Publisher(models.Model):
    name = models.CharField(max_length=100,null=False)
    address = models.CharField(max_length=100,null=False)

class Article(models.Model):
    name = models.CharField(max_length=100,null=False,db_column='article_name')
    email = models.EmailField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'articles'
        ordering = ['-pub_date']

