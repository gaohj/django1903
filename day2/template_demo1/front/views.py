from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
# Create your views here.
def index(request):
    html = render_to_string('index.html')
    return HttpResponse(html)

def list(request):
    return render(request,'test.html')
