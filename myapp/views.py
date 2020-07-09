#coding=utf-8

from django.shortcuts import render
from myapp.mysql import connect
from myapp.models import User
from handle.write_letter import save
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
import json
#import time,simplejson,json,os,commands

# Create your views here.
def index(request):
    return render(request,'base.html')

#http://127.0.0.1:8082/api
# 0 失败 1 成功 register
def api(req):
    if req.method == "POST":
        dic = req.GET.dict()
        print(dic)
        username = dic['username']
        password = dic['password']
        email = dic['email']
    sql='''select * from myapp_user where username="{}"'''.format(username)
    res=connect(sql)
    re=1
    for u in res:
        print('用户存在')
        re=0
        return HttpResponse('%d'%(re))
    User.objects.create(
        username=username,
        password=password,
        email=email
    )
    return HttpResponse('%d'%(re))

#登陆模块
def login(req):
    if req.method == "POST":
        dic = req.GET.dict()
        print(dic)
        username = dic['username']
        password = dic['password']
    sql='''select *  from myapp_user where username="{}" and password="{}" '''.format(username,password)
    res=connect(sql)
    data = username
    flag = 0
    for i in res:
        loginbean = {}
        loginbean['username'] = username
        req.session['loginbean'] = loginbean
        flag = json.dumps(loginbean)
        print(flag)
    return HttpResponse(flag,content_type='application/json')
def write_letter(req):
    if req.method == "POST":
        username = req.POST.get("username", None)
        context=req.POST.get("context", None)
        letter_topic=req.POST.get("letter_topic",None)
        right = req.POST.get("right", None)
        flag = req.POST.get("flag", None)
    username="lidan"
    context="这是一个内容文档"
    letter_topic="0"
    right="0"
    flag="0"
    data=[username,context,letter_topic,right,flag]
    save(data)
    return JsonResponse({"status": 200, "msg": "OK", "data":0 })
#http://127.0.0.1:8001/all_message/?page=9
def all_message(req):
    page_num=req.GET.get('page')
    print(page_num)
    # if req.method == "POST":
    #     letter_topic = req.POST.get("letter_topic", None)

    # sql='''select * from myapp_letter where letter_topic="{}"'''.format(letter_topic)
    # res=connect(sql)
    # for i in res:
    #     print(i)
    return JsonResponse({"status": 200, "msg": "OK", "data":0})

def getSession(request):
    print(request.session)
    if 'loginbean' in request.session:
        loginbean =request.session['loginbean']
        return HttpResponse(json.dumps(loginbean))
    else:
        return HttpResponse(0)

def logout(request):
    print(request.session)
    if 'loginbean' in request.session:
        del request.session['loginbean']
    return HttpResponse(1)