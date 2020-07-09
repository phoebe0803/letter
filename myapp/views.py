#coding=utf-8

from django.shortcuts import render
from myapp.mysql import connect
from myapp.models import User
from handle.write_letter import save
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect

#import time,simplejson,json,os,commands

# Create your views here.
def index(request):
    return render(request,'base.html')

#http://127.0.0.1:8082/api
def api(req):
    if req.method == "POST":
        username = req.POST.get("username", None)
        password = req.POST.get("password", None)
        email = req.POST.get("email", None)
    username=""
    password="123"
    email="123@qq.com"
    sql='''select * from myapp_user where username="{}"'''.format(username)
    res=connect(sql)
    for u in res:
        print(u)
        return JsonResponse({ "data": "用户存在"})
    User.objects.create(
        username=username,
        password=password,
        email=email
    )
    data=username
    return JsonResponse({"status": 200, "msg": "OK", "data": data})
#登陆模块
def login(req):
    if req.method == "POST":
        username = req.POST.get("username", None)
        password = req.POST.get("password", None)
    username="lidan"
    password="123"
    sql='''select *  from myapp_user where username="{}" and password="{}" '''.format(username,password)
    res=connect(sql)
    data = username
    for i in res:
        print("登陆成功")
        return JsonResponse({"status": 200, "msg": "登陆成功", "data": data})

    return JsonResponse({"status": 200, "msg": "登陆失败，用户名或者密码错误", "data": data})
def write_letter(req):
    if req.method == "POST":
        username = req.POST.get("username", None)
        context=req.POST.get("context", None)
        letter_topic=req.POST.get("letter_topic",None)
        right = req.POST.get("right", None)
        flag = req.POST.get("flag", None)
    username="lidan"
    context="这是一个内容文档"
    letter_topic="爱情"
    right="0"
    flag="0"
    data=[username,context,letter_topic,right,flag]
    save(data)
    return JsonResponse({"status": 200, "msg": "OK", "data":0 })
def all_message(req):
    sql='''select * from myapp_letter '''
    res=connect(sql)
    for i in res:
        print(i)
    return JsonResponse({"status": 200, "msg": "OK", "data":0})

