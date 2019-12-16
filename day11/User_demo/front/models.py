from django.db import models
from django.contrib.auth.models import PermissionsMixin,BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
# Create your models here.

class UserManager(BaseUserManager):
    def _create_user(self, telephone,username,password, **kwargs):
        if not telephone:
            raise ValueError('必须传手机号码')
        if not password:
            raise ValueError('必须传密码')
        user = self.model(telephone=telephone,username=username)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,telephone,username, password, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username,password=password,**kwargs)

    def create_superuser(self, telephone,username,password, **kwargs):
        kwargs['is_staff']= True
        kwargs['is_superuser'] = True
        return self._create_user(telephone=telephone, username=username, password=password, **kwargs)


class User(AbstractBaseUser,PermissionsMixin):
    telephone = models.CharField(max_length=100,unique=True)
    email = models.CharField(max_length=100,unique=True)
    username = models.CharField(max_length=100,unique=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = []

    objects = UserManager()
    def get_full_name(self):
        return self.username

