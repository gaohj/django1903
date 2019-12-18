#encoding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField

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

    def create_user(self,telephone, username, password,email=None, **kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(telephone=telephone,username=username, email=email, password=password, **kwargs)

    def create_superuser(self, telephone,username, password,email=None, **kwargs):
        kwargs['is_superuser'] = True
        kwargs['is_staff'] = True
        return self._create_user(telephone=telephone, username=username, email=email, password=password, **kwargs)


class User(AbstractBaseUser,PermissionsMixin):
    #主键不采用 自增id的形式  id 101 102 103 104
    #uuid 太长  uuid.uuid4()
    #pip install django-shortuuidfield
    uid = ShortUUIDField(primary_key=True)
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True,null=True)
    username = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'telephone'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username