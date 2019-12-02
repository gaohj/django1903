# Django第一天   

> 2003年demo版 2005年正式版  目的为了节约开发时间的  因为超级好用 慢慢被多加公司使用
>
> Instagram 豆瓣 知乎 等都使用 django 
>
> 内置强大的用户系统 以及权限系统  

## django 版本 和 python版本  

| django 版本 | python版本          |
| ----------- | ------------------- |
| 1.8         | 2.7 3.2 3.3 3.4 3.5 |
| 1.9 1.0     | 2.7 3.4 3.5         |
| 1.11        | 2.7 3.4 3.5 3.6     |
| 2.0         | 3.4 3.5 3.6         |
| 2.1         | 3.5 3.6 3.7         |

## web服务器  应用服务器  web应用框架  

###  web服务器   

> 直接响应 用户的请求   端口号默认80  如果是静态的资源 比如 静态页面  js css  图片都能直接返回

* nginx 
* apache
* lighthttpd 
* IIS windows系统 适用的  

### 应用服务器 

> 动态的逻辑需要 python j2ee php等代码去实现  nginx 不能直接发起调用python去处理 需要通过 应用服务器  uwsgi   gunicorn tomcat （java）它们交给 python    



### web应用框架  

> 封装了常用的web功能  叫好比是 毛坯房加上一些 基本的 家用电器等  

```
快速的搭建起 我们的web产品 
```



## 设计模式 MVC MTV  

* M model 模型        M  model 模型  一个数据表 一个模型  
* V  view 视图          T  template 模板   一个页面      
* C  controller 控制器      V  view 视图     



## URL 组成部分 

> uniform resource locator 统一资源定位符  

```
scheme://host:port/path?query-string=xxx#anchor
```

`scheme`:访问的协议  http 80 https  443 ftp 21  都是基于TCP/IP协议 

`host`:域名 或者 ip  

`port`:端口号  系统0~65535个端口  0~127 被占用  自定义端口号 选择  1024 以后的  

`path`: 路由地址   https://www.jianshu.com/writer#/   writer就是 path 

`query-string`:  https://www.baidu.com/s?wd=nba  wd=nba   就是查询字符串   

 https://www.baidu.com/?username=test&password=123456  ?username=test&password=123456   get方式 携带参数  

`anchor`: 当页面太大  悬浮框保持不动 可以跳到指定的位置  



注意: url 中所有的字符集都是 ASCII字符集  如果出现中文 那么浏览器先编码再传输

## 配置pycharm远程虚拟环境

```
├── django_first
│   ├── __init__.py
│   ├── settings.py  #项目的设置文件  跟项目所有相关的配置全部写到这里
│   ├── urls.py    #配置项目路由  我们要把我们的方法 暴露出去 需要 在这里配置 
│   └── wsgi.py    #部署上线的时候 用到  
└── manage.py #和项目交互 基本上都是基于这个文件  一般在命令行输入 python manage.py  
	python manage.py help #可以具体看做什么事情  除非你相当清楚 否则别编辑  


python  
```



## 安装  django  

> pip install django==2.0  

## 创建项目 

> 架子 

```
1.切换到虚拟环境  
2.切换到指定的目录  
3.django-admin startproject 项目名称   
```

## 创建应用  

> 豆瓣电影  有读书模块 、电影模块、音乐模块  这三个体现在 djang上就是  一个个的应用 
>
> 一个项目中可以有多个app  

```
python manage.py startapp 应用名称 
```



## 启动  

```shell
修改settings.py 

ALLOWED_HOSTS = ['服务器的ip','127.0.0.1'] #比如服务器的ip是 192.168.58.40

切换到项目的根目录   

python manage.py runserver 0.0.0.0:9000 # 阿里云服务器 一定要开启9000端口 
```



##　视图　　

> 一般卸载 应用下面的 views 中  第一个参数永远是request  这个request 是 HttpRequest的一个对象  包含前端用户所有的请求  参数  header  表单 等信息     request 接收前端传过来的数据  保存到数据库中  最后把执行的结果返回给浏览器   
>
> 返回结果必须是HttpResponse 

```python
from django.http import HttpResponse,HttpRequest

# Create your views here.
def book(request):
    #request接收前端用户所有的请求
    return HttpResponse("图书首页")


```



## URL映射 

> 项目settings.py 中  
>
> ```python
> ROOT_URLCONF = 'django_second.urls'  #表示会来这里读取匹配规则
> ```
>
> 将上面的视图函数 暴露出去的过程  
>
> urls.py文件中   有一个 urlpatterns 变量  django会从这里读取所有的匹配规则  

```python
from book.views import book
urlpatterns = [
    ...
    path('book/', book),
]
```



## 给 URL传递参数 

>  http://192.168.58.40:9000/book/detail/100/20000/ 

views.py 

```python
def book_detail(request,book_id,category_id): 
    text = "您想要查看的文章id为%s,图书分类是:%s" % (book_id,category_id)
    return HttpResponse(text)
```

urls.py

```
from book import views
urlpatterns = [
    ...
    path('book/detail/<book_id>/<category_id>/', views.book_detail),

]
```



　

