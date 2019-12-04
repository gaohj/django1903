from django import template
from datetime import datetime
#创建python包 命名为templatetags
#过滤器至多有两个参数
#第一个参数永远是被过滤的那个值
#{{被过滤的值|过滤器:参数}}
#写完之后进行注册 django.template.Library.filter
#将应用注册到settings.py中的INSTALLED_APPS中
register = template.Library()
@register.filter
def greet(value,word):
    return value+word
@register.filter
def time_since(value):
    """

    :param value: 发表的时间
    :return: 修饰过后的值
    1分钟内 刚刚
    大于1分钟 小于1小时  xx分钟前
    大于1小时 小于24小时 xx小时前
    大于24小时 小于30天  xx天前
    显示具体的时间  年月日时分秒
    """
    if not isinstance(value,datetime):
        return value
    now = datetime.now()
    timestamp = (now-value).total_seconds()
    if timestamp < 60:
        return '刚刚'
    elif timestamp >=60 and timestamp < 60 *60:
        minute = int(timestamp/60)
        return '%s分钟前' % minute
    elif timestamp >=60*60 and timestamp < 60 *60*24:
        hour = int(timestamp/60*60)
        return '%s小时前' % hour
    elif timestamp >=60*60*24 and timestamp < 60 *60*24*30:
        day = int(timestamp/60*60*24)
        return '%s天前' % day
    else:
        return value.strftime("%Y/%m/%d %H:%M:%s")