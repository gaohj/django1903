from django import forms
from django.core import validators
from .models import User

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=20,label="标题",min_length=6,error_messages={"max_length":"最常不超过20字符","min_length":"最短不超过6字符"})
    content = forms.CharField(widget=forms.Textarea,label='内容')
    email = forms.EmailField(label="邮箱")
    reply = forms.BooleanField(required=False,label="回复")

class MyForm(forms.Form):
    # email = forms.EmailField(error_messages={"invalid":"请输入正确的邮箱"})
    price = forms.FloatField(error_messages={"invalid":"请输入正确的价格"})
    personal_website = forms.URLField(error_messages={"invalid":"请输入正确的url地址","required":"请输入个人网站"})
    email = forms.CharField(validators=[validators.EmailValidator(message="请输入正确的邮箱地址")])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}',message="请输入正确的手机号")])

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="标题", min_length=6,error_messages={"max_length": "最常不超过20字符", "min_length": "最短不超过6字符"})
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[3456789]\d{9}', message="请输入正确的手机号")])
    password1 = forms.CharField(max_length=30,min_length=6)
    password2 = forms.CharField(max_length=30,min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError('改手机号已经存在了')
        return telephone
    #当走到clean()方法表示 每个字段都验证成功了
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('两次密码不一致')
        return cleaned_data




