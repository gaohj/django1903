from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return '<category:(id:%s,name:%s)>' % (self.id,self.name)
    class Meta:
        db_table = 'category'


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,related_name="articles")
    create_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '<article:(title:%s,content:%s,create_time:%s)>' % (self.title,self.content,self.create_time)
    class Meta:
        db_table = 'article'

