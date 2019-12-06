from django.db import models

# Create your models here.

class FrontUser(models.Model):
    username = models.CharField(max_length=100)
    def __str__(self):
        return "<User:(id:%s,username:%s)>" % (self.id,self.username)
