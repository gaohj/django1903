from django.db import models
from django.core import validators

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.FileField(upload_to='files',validators=[validators.FileExtensionValidator(['txt','md','jpg','wmv'],message='缩略图必须是指定格式的文件')])
    # thumbnail = models.ImageField(upload_to='files')
    # thumbnail = models.ImageField(upload_to='%Y/%m/%d')
