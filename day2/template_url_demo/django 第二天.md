#  django 第二天  

* 复习 
* 模板 
  * 变量
  * 常用标签 
  * 过滤器 
  * 模板架构 
  * 静态文件   



## url 命名、应用命名空间、实例命名空间   

### url 命名

> 为了避免每次跳转  地址写死 后期维护困难  所以给url起名字  通过url的名字 可以反转拿到 对应的路径 

```python
views.py 
	from django.http import HttpResponse
from django.shortcuts import redirect,reverse

# Create your views here.
#http://192.168.58.40;9000/?username=zpc
def index(request):
    #接收参数的值
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        # return redirect('/login/')
        login_url = reverse('login')
def login(request):
    return  HttpResponse('前台登录页')

urls.py 
	from django.urls import path
	from . import views
    urlpatterns = [
        path('',views.index,name='index'),
        path('signin/',views.login,name='login')
    ]
```



### 应用命名空间 

> 如果说 两个app的 url的名称一致 容易导致 跳转 混乱  解决方案  应用命名空间   每个应用的 urls.py
>
> 七个名字  实例如下  

```python
urls.py 
	from django.urls import path
    from . import views
    app_name = 'cms'
    urlpatterns = [
        path('',views.index,name='index'),
        path('signin/',views.login,name='login')
    ]
views.py 
	from django.http import HttpResponse
    from django.shortcuts import redirect,reverse

    # Create your views here.
    #http://192.168.58.40;9000/?username=zpc
    def index(request):
        #接收参数的值
        username = request.GET.get('username')
        if username:
            return HttpResponse('前台首页')
        else:
            # return redirect('/login/')
            login_url = reverse('front:login')  #应用命名空间:url名称
            print("*"*30)
            print(login_url)
            print("*"*30)
            return redirect(login_url)
    def login(request):
        return  HttpResponse('前台登录页')
```



### 实例命名空间 

> 如果项目中有不同的需求 两个不同的地址 同时 登录一个后台  如果没有登录 应该分别跳转到对应的登录页  
>
> 实现方式 如下  

```python
views.py  
    from django.http import HttpResponse
    from django.shortcuts import redirect,reverse

    # Create your views here.
    #http://192.168.58.40;9000/?username=zpc
    def index(request):
    #接收参数的值
    	username = request.GET.get('username')
        if username:
            return HttpResponse('<h1>后台cms首页</h1>')
        else:
            #获取当前实例
            current_namespace = request.resolver_match.namespace
            return redirect(reverse('%s:login'%current_namespace))
            # return redirect(login_url)
    def login(request):
    return  HttpResponse('后台登录页')

urls.py 这里是 主url文件  
    from django.urls import path,include

    urlpatterns = [
        ...
        path('cms1/',include('cms.urls',namespace='cms1')), #写在include里边 
        path('cms2/',include('cms.urls',namespace='cms2'))
    ]

```



## 自定义url转化器   

> 延后 讲  



## 渲染模板  

* render_to_string 

  将模板编译后 渲染成 python的字符串格式 再通过HttpResponse类  包装成 HttpResponse对象 返回给 前台

  ```python
  from django.http import HttpResponse
  from django.template.loader import render_to_string
  
  # Create your views here.
  def index(request):
      html = render_to_string('index.html')
      return HttpResponse(html)
  ```

  

* render 

  >
  >
  >将模板编译后 渲染成 python的字符串格式 再通过HttpResponse类  包装成 HttpResponse对象 返回给 前台   合并成一起   

  ```
  def list(request):
      return render(request,'test.html')
  ```

## 模板加载顺序   

`以 front应用  views.py  render(request,'test.html')为例子`

* 先到 settings.py中 DIRS 下面查找  test.html 有 没有 如果有就返回  如果没有 查看 settings.py APP_DIRS
* APP_DIRS 默认为True 表铭 会到 settings.py INSTALLED_APPS 下也就是安装的应用下面 templates下面查找 有没有没有test.html 
* 这里先找 front 应用下面  fro  nt应用 注册了 如果front应用里边没有 test.html 
* 但是 注册的应用列表中 cms 下面有test.html   那么就会渲染 cms下面的 templates下面的 test.html 

## 坑  

> diango2.0 最大支持到3.6（不支持3.6.8）  建议3.6.6 
>
> django2.1 最大支持到3.7  



## 模板变量渲染  

> 在模板中使用 变量   {{ 变量名}}
>
> {# 注释 #}

```
def index(request):
    return render(request,'index.html',context={'username':'kangbazi'})
 
 
页面上 {{username}}
```



### 访问对象的属性  

> 可以通过  {{对象.属性名}}

```python
from django.shortcuts import render
class Person(object):
    def __init__(self,username):
        self.username = username
def index(request):
    p = Person('赵鹏程')
    context = {
        'person':p
    }
    return render(request,'index.html',context=context)

模板上   {{ person.username }}
```

### 访问字典的key 对应的 value  

```python
from django.shortcuts import render

def index(request):
     context = {
        'persons':{
            'username':'kangbazi',
            'password':'123456'
        }
     }
    return render(request,'index.html',context=context)

模板上: 
    {{ persons.username }}
    {{ persons.password }}
```

### 访问元组 或者列表   .的方式   

```
def index(request):
    context = {
        'persons':(
            '张三',
            '李四',
            '王五',
        )
    }
    return render(request,'index.html',context=context)
    
    
{{persons.1}}
```



## 常用标签   

### if 

>  所有的标签  用 {%%}包裹  
>
> 可以使用 == != <  <=  >= in not in  is  is not 等运算符  

```
1.运算符  
context = {
        'age':16
    }
    
{% if age < 18  %}
    <p>未成年不能撸</p>
    {% elif age == 18 %}
    <p>小撸怡情</p>
    {% else %}
    <p>樯橹灰飞烟灭</p>
{% endif %}

2.in not in   
 context = {
        'heros':[
            '赵云',
            '亚索',
            '关二爷'
        ]
    }

{% if '关二爷' in heros %}
        <p>正在待命</p>
    {% else %}
        <p>关二爷累了</p>
    {% endif %}
```



### for ...in...  元组、字典、列表、字符串等  

#### 遍历字典 

```
context = {
        'persons':{
            'username':'kangbazi',
            'sex':0,
            'height':'179cm'
        }
}
<ul>
{% for key,value in persons.items%}
<li>{{ key }}/{{ value }}</li>
{% endfor %}
</ul>

```

#### 遍历列表

```python
context = {
        'persons':[
            '张三',
            '李四',
            '王五',
            '赵六',
            '老气',
        ]
    }
    
  <ul>
        {% for person in persons reversed%}#reversed表示倒叙显示的意思   
            <li> {{ person }}</li>
        {% endfor %}
    </ul>
```



### for循环 变量  

* forloop.counter 当前循环的下标  默认 1开始 
* forloop.counter0 当前循环的下标  默认 0开始
* forloop.recounter 当前循环的反向下标  最后一个是1 
* forloop.recounter0 当前循环的反向下标  最后一个是0
* forloop.first 是否是第一次遍历 
* forloop.last 是否是最后一次遍历
* forloop.parentloop 多层循环嵌套 代表上一个for循环  

```python
views.py 
  context = {
        'books':[
            {
              'name':'三国演义',
              'author':'罗贯中',
              'price':100
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 99
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 98
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 101
            }
        ]
    }
    
模板

	        <thead>
            <tr>
                <th>序号</th>
                <th>书名</th>
                <th>作者</th>
                <th>价格</th>
            </tr>
        </thead>
        <tbody>
            {% for book in books %}
                {% if forloop.first %}
                    <tr style="background: pink">
                    {% elif forloop.last %}
                    <tr style="background: green">
                {% else%}
                <tr>
                {% endif %}
                    <td>{{ forloop.counter }}</td>
                    <td>{{ book.name }}</td>
                    <td>{{ book.author }}</td>
                    <td>{{ book.price }}</td>
                </tr>

            {% endfor %}

        </tbody>
    </table>
```

#### empty 

```python
   context = {
        'comments':[
            'test',
            'test1',
            'test2'
        ]
    }
    
   模板上： 
   	 <ul>
    {% for comment in comments %}

        <li> {{ comment }}</li>
     {% empty %}
        <li>没有任何内容</li>
    {% endfor %}
    </ul>
```

### with

```python
 	
 	context = {
        'comments':[
            'test',
            'test1',
            'test2'
        ]
    }
 	{% with tt=comments.1 %}
            <li>{{ tt }}</li>
            <li>{{ tt }}</li>
            <li>{{ tt }}</li>
            <li>{{ tt }}</li>
        {% endwith %}
            <li>{{ tt }}</li>  #出了with标签就不适用了 

        {% with comments.1 as ttt  %}
            <li>{{ ttt }}</li>
            <li>{{ ttt }}</li>
            <li>{{ ttt }}</li>
            <li>{{ ttt }}</li>
        {% endwith %}
```

# 常用的模板标签：

1. `if`标签：`if`标签相当于`Python`中的`if`语句，有`elif`和`else`相对应，但是所有的标签都需要用标签符号（`{%%}`）进行包裹。`if`标签中可以使用`==、!=、<、<=、>、>=、in、not in、is、is not`等判断运算符。示例代码如下：

   ```python
    {% if "张三" in persons %}
        <p>张三</p>
    {% else %}
        <p>李四</p>
    {% endif %}
   ```

2. `for...in...`标签：`for...in...`类似于`Python`中的`for...in...`。可以遍历列表、元组、字符串、字典等一切可以遍历的对象。示例代码如下：

   ```python
    {% for person in persons %}
        <p>{{ person.name }}</p>
    {% endfor %}
   ```

   如果想要反向遍历，那么在遍历的时候就加上一个`reversed`。示例代码如下：

   ```python
    {% for person in persons reversed %}
        <p>{{ person.name }}</p>
    {% endfor %}
   ```

   遍历字典的时候，需要使用`items`、`keys`和`values`等方法。在`DTL`中，执行一个方法不能使用圆括号的形式。遍历字典示例代码如下：

   ```python
    {% for key,value in person.items %}
        <p>key：{{ key }}</p>
        <p>value：{{ value }}</p>
    {% endfor %}
   ```

   在`for`循环中，`DTL`提供了一些变量可供使用。这些变量如下：

   - `forloop.counter`：当前循环的下标。以1作为起始值。
   - `forloop.counter0`：当前循环的下标。以0作为起始值。
   - `forloop.revcounter`：当前循环的反向下标值。比如列表有5个元素，那么第一次遍历这个属性是等于5，第二次是4，以此类推。并且是以1作为最后一个元素的下标。
   - `forloop.revcounter0`：类似于forloop.revcounter。不同的是最后一个元素的下标是从0开始。
   - `forloop.first`：是否是第一次遍历。
   - `forloop.last`：是否是最后一次遍历。
   - `forloop.parentloop`：如果有多个循环嵌套，那么这个属性代表的是上一级的for循环。

3. `for...in...empty`标签：这个标签使用跟`for...in...`是一样的，只不过是在遍历的对象如果没有元素的情况下，会执行`empty`中的内容。示例代码如下：

   ```python
    {% for person in persons %}
        <li>{{ person }}</li>
    {% empty %}
        暂时还没有任何人
    {% endfor %}
   ```

4. `with`标签：在模版中定义变量。有时候一个变量访问的时候比较复杂，那么可以先把这个复杂的变量缓存到一个变量上，以后就可以直接使用这个变量就可以了。示例代码如下：

   ```python
    context = {
        "persons": ["张三","李四"]
    }
   
    {% with lisi=persons.1 %}
        <p>{{ lisi }}</p>
    {% endwith %}
   ```

   有几点需要强烈的注意：

   - 在`with`语句中定义的变量，只能在`{%with%}{%endwith%}`中使用，不能在这个标签外面使用。

   - 定义变量的时候，不能在等号左右两边留有空格。比如`{% with lisi = persons.1%}`是错误的。

   - 还有另外一种写法同样也是支持的：

     ```python
       {% with persons.1 as lisi %}
           <p>{{ lisi }}</p>
       {% endwith %}
     ```

5. `url`标签：在模版中，我们经常要写一些`url`，比如某个`a`标签中需要定义`href`属性。当然如果通过硬编码的方式直接将这个`url`写死在里面也是可以的。但是这样对于以后项目维护可能不是一件好事。因此建议使用这种反转的方式来实现，类似于`django`中的`reverse`一样。示例代码如下：

   ```python
   <a href="{% url 'url的名字不是路由的名字' %}"></a>
   <a href="{% url 'book:list' %}">图书列表页面</a>
   ```

   如果`url`反转的时候需要传递参数，那么可以在后面传递。但是参数分位置参数和关键字参数。位置参数和关键字参数不能同时使用。示例代码如下：

   ```python
        # path部分
        path('detail/<book_id>/',views.book_detail,name='detail')
   
        # url反转，使用位置参数
        <a href="{% url 'book:detail' 1 %}">图书详情页面</a>
   
        # url反转，使用关键字参数
        <a href="{% url 'book:detail' book_id=1 %}">图书详情页面</a>
   ```

   如果想要在使用`url`标签反转的时候要传递查询字符串的参数，那么必须要手动在在后面添加。示例代码如下：

   ```python
        <a href="{% url 'book:detail' book_id=1 %}?page=1">图书详情页面</a>
   ```

   如果需要传递多个参数，那么通过空格的方式进行分隔。示例代码如下：

   ```python
        <a href="{% url 'book:detail' book_id=1 page=2 %}">图书详情页面</a>
   ```

6. `spaceless`标签：移除html标签中的空白字符。包括空格、tab键、换行等。示例代码如下：

   ```python
    {% spaceless %}
        <p>
            <a href="foo/">Foo</a>
        </p>
    {% endspaceless %}
   ```

   那么在渲染完成后，会变成以下的代码：

   ```html
    <p><a href="foo/">Foo</a></p>
   ```

   `spaceless`只会移除html标签之间的空白字符。而不会移除标签与文本之间的空白字符。看以下代码：

   ```python
    {% spaceless %}
        <strong>
            Hello
        </strong>
    {% endspaceless %}
   ```

   这个将不会移除`strong`中的空白字符。

7. `autoescape`标签：开启和关闭这个标签内元素的自动转义功能。自动转义是可以将一些特殊的字符。比如`<`转义成`html`语法能识别的字符，比如`<`会被转义成`&lt;`，而`>`会被自动转义成`&gt;`。模板中默认是已经开启了自动转义的。`autoescape`的示例代码如下：

   ```python
    # 传递的上下文信息
    context = {
        "info":"<a href='www.baidu.com'>百度</a>"
    }
   
    # 模板中关闭自动转义
    {% autoescape on %}
        {{ info }}
    {% endautoescape %}
   ```

   那么就会显示百度的一个超链接。如果把`on`成`off`，那么就会显示成一个普通的字符串。示例代码如下：

   ```python
    {% autoescape on %}
        {{ info }}
    {% endautoescape %}
   ```

8. `verbatim`标签：默认在`DTL`模板中是会去解析那些特殊字符的。比如`{%`和`%}`以及`{{`等。如果你在某个代码片段中不想使用`DTL`的解析引擎。那么你可以把这个代码片段放在`verbatim`标签中。示例代码下：

   ```python
    {% verbatim %}
        {{if dying}}Still alive.{{/if}}
    {% endverbatim %}
   ```

9. 更多标签请参考官方文档：`https://docs.djangoproject.com/en/2.0/ref/templates/builtins/`