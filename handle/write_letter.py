#coding=utf-8
from myapp.mysql import connect
from myapp.models import Letter
def save(data):
    Letter.objects.create(
        username=data[0],
        context=data[1],
        letter_topic=data[2],
        right=data[3],
        flag=data[4]
    )
    print(data)