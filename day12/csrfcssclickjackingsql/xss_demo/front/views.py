from django.shortcuts import render,redirect,reverse
from . models import Comment
# Create your views here.
def index(request):
    context = {
        'comments':Comment.objects.all()
    }
    return render(request,'index.html',context=context)

def add_comment(request):
    content = request.POST.get('content')
    Comment.objects.create(content=content)
    return redirect(reverse('index'))


