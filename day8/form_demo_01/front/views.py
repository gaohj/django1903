from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
# Create your views here.

class IndexView(View):
    def get(self,request):
        form = MessageBoardForm()
        return render(request,'index.html',context={"form":form})