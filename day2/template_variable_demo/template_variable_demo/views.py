from django.shortcuts import render
class Person(object):
    def __init__(self,username):
        self.username = username
def index(request):
    p = Person('赵鹏程')
    # return render(request,'index.html',context={'username':'kangbazi'})
    # context = {
    #    'persons':{
    #        'username':'kangbazi',
    #        'password':'123456'
    #    }
    # }
    # context = {
    #     'person':p
    # }
    context = {
        'persons':(
            '张三',
            '李四',
            '王五',
        )
    }
    return render(request,'index.html',context=context)