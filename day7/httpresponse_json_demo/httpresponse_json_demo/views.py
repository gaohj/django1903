from django.http import HttpResponse,JsonResponse
import json
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