from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import Article
from .forms import ArticleForm
# Create your views here.
class IndexView(View):
    def get(self,request):
        return render(request,'index.html')
    # def post(self,request):
    #     myfile = request.FILES.get('thumbnail')
    #     with open('someone.txt','wb') as fp:
    #         for chunk in myfile.chunks():
    #             fp.write(chunk)
    #     return HttpResponse('success')
    # def post(self,request):
    #     myfile = request.FILES.get('thumbnail')
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     Article.objects.create(title=title,thumbnail=myfile,content=content)
    #     return HttpResponse('success')

    def post(self,request):
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')