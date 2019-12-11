#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import  render

def view_403(request):
    return render(request,'errors/403.html',status=403)

def view_405(request):
    return render(request,'errors/405.html',status=405)