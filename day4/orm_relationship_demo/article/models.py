from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)
# Create your models here.
#分类 文章
#1个分类下面 多篇文章
#一篇文章 只能属于一个分类
#分类是1
#文章是多
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category",on_delete=models.CASCADE,null=True,related_name='articles')
    author = models.ForeignKey("frontuser.FrontUser",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return "<Article:(id:%s,title:%s,content:%s)>" %(self.id,self.title,self.content)