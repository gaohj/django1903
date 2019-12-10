from django.http import HttpResponse,JsonResponse,StreamingHttpResponse
import json
import csv
from django.template import loader
def index(request):
    # response = HttpResponse('<h1>千锋扛把子</h1>')
    response = HttpResponse('<h1>千锋扛把子</h1>',content_type="text/plain;charset=utf-8")
    response.status_code = 404
    response.content = '我们的班花也是千锋的班花,也是金融港的班花,江夏区，武汉，全中国'
    response['X-Token'] = 'kangbazi'
    return response

def jsonresponse_view(request):
    persons = [
        {
            'username':'xinxinxiangrong',
            'password':'123456',
            'age':18,
            'sex':0
        },
        {
            'username': 'chengcheng',
            'password': '123321',
            'age': 20,
            'sex': 1
        }
    ]
    # person_str = json.dumps(persons)
    # response = HttpResponse(person_str,content_type='application/json')
    # return response
    response = JsonResponse(persons,safe=False)
    return response

def csv_demo(request):
    #告诉浏览器 这是一个csv 文件 不是  html文件
    response = HttpResponse(content_type='text/csv')
    #添加head头 Content-Disposition  设置为attachment 告诉浏览器 这是个附件 不再对文件
    #进行显示 而是直接下载  附件名是  1903.csv
    response['Content-Disposition'] = 'attachment;filename="1903.csv"'
    #使用csv的writer方法 将数据写入 response
    writer = csv.writer(response)
    writer.writerow(['username','age','sex','height'])
    writer.writerow(['kangbazi','18','0','181cm'])

    return response


def template_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="someone.csv"'

    context = {
        'rows':[
            ['username','password','age'],
            ['zhangsan','123456','18'],
            ['lisi','123123','19'],
        ]
    }
    template = loader.get_template('kangbazi.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response


def large_csv_view(request):
    # response = HttpResponse(content_type='text/csv')
    # response['Content-Disposition'] = 'attachment;filename="large.csv"'
    # writer = csv.writer(response)
    # for row in range(0,1000000):
    #     writer.writerow(['Row {}'.format(row),'{}'.format(row)])
    # return response
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="large_stream.csv"'
    rows = ("Row {},{}\n".format(row,row) for row in range(0,1000000))
    response.streaming_content = rows
    return response

