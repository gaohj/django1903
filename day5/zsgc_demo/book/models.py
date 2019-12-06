from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100,null=False)
    author = models.CharField(max_length=100,null=False)
    price = models.FloatField(default=0)


    def __str__(self):
        return "<Book:(name:%s author:%s price:%s)>" % (self.name,self.author,self.price)

    class Meta:
        db_table = 'books'
        ordering = ['-price']

