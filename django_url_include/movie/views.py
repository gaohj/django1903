from django.http import HttpResponse

# Create your views here.
def movie(request):
    return HttpResponse('电影首页')
def movie_detail(request,movie_id):
    text = '电影id是:%s' % movie_id
    return HttpResponse(text)
def movie_list(request):
    return HttpResponse('电影列表')