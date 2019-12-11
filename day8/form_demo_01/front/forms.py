from django import forms

class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=20,label="标题",min_length=6,error_messages={"max_length":"最常不超过20字符","min_length":"最短不超过6字符"})
    content = forms.CharField(widget=forms.Textarea,label='内容')
    email = forms.EmailField(label="邮箱")
    reply = forms.BooleanField(required=False,label="回复")