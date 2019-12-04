from django.shortcuts import render
from datetime import datetime
# Create your views here.
def index(request):
    context = {
        'value':'班花鹏程兄',
        'times': datetime(year=2019,month=12,day=4,hour=8,minute=18,second=19)
    }
    return render(request,'index.html',context=context)
