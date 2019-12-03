from django.shortcuts import render
def index(request):
    # return render(request,'index.html',context={'username':'kangbazi'})
    context = {
       'persons':{
           'username':'kangbazi',
           'password':'123456'
       }
    }
    return render(request,'index.html',context=context)