from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
# class Person(User):
#     # telephone = models.CharField(max_length=11)
#     class Meta:
#         proxy = True
#
#     @classmethod
#     def get_blacklist(cls):
#         return cls.objects.filter(is_active=False)

# class UserExtension(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="extension")
#     telephone = models.CharField(max_length=11)
#     school = models.CharField(max_length=100)
#
# @receiver(post_save,sender=User)
# def handler_user_extension(sender,instance,created,**kwargs):
#     if created:
#         UserExtension.objects.create(user=instance)
#     else:
#         instance.extension.save()

class UserManager(BaseUserManager):
    def _create_user(self, telephone,username, email, password, **kwargs):
        if not telephone:
            raise ValueError('The given telephone must be set')
        if not username:
            raise ValueError('The given username must be set')
        if not password:
            raise ValueError('The given password must be set')
        user = self.model(telephone=telephone,username=username, email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, telephone,username, email=None, password=None, **kwargs):
        kwargs['is_superuser'] =False
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)

    def create_superuser(self, telephone,username, email, password, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)


class User(AbstractUser):
    telephone = models.CharField(max_length=11,unique=True)
    school = models.CharField(max_length=100)

    USERNAME_FIELD = 'telephone'

    objects = UserManager()