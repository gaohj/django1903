#encoding:utf-8

from django import forms
from django.contrib.auth import get_user_model
from django.core import validators

class LoginForm(forms.ModelForm):
    remember = forms.IntegerField(required=False)
    telephone = forms.CharField(max_length=11,validators=[validators.RegexValidator(r'1[3456789]\d{9}',message="{'invalid':'请输入正确的手机号码'}")])
    class Meta:
        model = get_user_model()
        fields = ['password']
