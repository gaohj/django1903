from django.shortcuts import render

def index(request):
    # context = {
    #     'age':16
    # }
    # context = {
    #     'heros':[
    #         '赵云',
    #         '亚索',
    #         '关二爷'
    #     ]
    # }
    # context = {
    #     'persons':{
    #         'username':'kangbazi',
    #         'sex':0,
    #         'height':'179cm'
    #     }
    # }
    # context = {
    #     'persons':[
    #         '张三',
    #         '李四',
    #         '王五',
    #         '赵六',
    #         '老气',
    #     ]
    # }
    # context = {
    #     'books':[
    #         {
    #           'name':'三国演义',
    #           'author':'罗贯中',
    #           'price':100
    #         },
    #         {
    #             'name': '水浒传',
    #             'author': '施耐庵',
    #             'price': 99
    #         },
    #         {
    #             'name': '西游记',
    #             'author': '吴承恩',
    #             'price': 98
    #         },
    #         {
    #             'name': '红楼梦',
    #             'author': '曹雪芹',
    #             'price': 101
    #         }
    #     ]
    # }
    context = {
        'comments':[
            'test',
            'test1',
            'test2'
        ]
    }
    return  render(request,'index.html',context=context)