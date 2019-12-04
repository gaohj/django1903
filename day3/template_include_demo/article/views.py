from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'username':'kangbazi'
    }
    return render(request, 'index1.html', context=context)

def school(request,names):
    context = {
        'name':names
    }
    return render(request,'school.html',context=context)

def company(request):
    nextis = request.GET.get('next')
    context = {
        'nextis':nextis
    }
    return render(request,'company.html',context=context)