from django.shortcuts import render
from datetime import datetime
# def index(request):
#     return render(request,'index.html')
# def index(request):
#     context = {
#         'info':'<script>alert("666")</script>'
#     }
#     return render(request,'index.html',context=context)
def index(request):
    return render(request,'index.html')
def add_view(request):
    context = {
        'x':['1','2','3'],
        'y':[4,'5','6']
    }
    return render(request,'add.html',context=context)

def cut_view(request):
    return render(request,'cut.html')

def date_view(request):
    context = {
        'today':datetime.now()
    }
    return render(request,'date.html',context=context)

def default_view(request):
    context = {
        'value':None
    }
    return render(request,'default.html',context=context)

def safe_view(request):
    context = {
        'text':'<script>alert("123321")</script>'
    }
    return render(request,'safe.html',context=context)

def truncate_view(request):
    context = {
        'text':'<p>武汉很大大到武昌汉口差异不是一般的大</p>'
    }
    return render(request,'truncate.html',context=context)