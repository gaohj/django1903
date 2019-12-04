from django.shortcuts import render
from django.db import connection
def index(request):
    cursor = connection.cursor()
    # cursor.execute("insert into book(name,author) values ('金瓶梅','生哥')")
    cursor.execute("select id,name,author from book")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return render(request,'index.html')