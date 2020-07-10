#coding=utf-8

from django.shortcuts import render
from myapp.mysql import connect
from myapp.models import User
from handle.letter import save,get_letter,get_all_letter,insert_collect_letter,delete_collect_letter_from_table
from handle.xinli import  get_message,get_xinli_all_message
from django.http import JsonResponse
from django.http import HttpResponse,HttpResponseRedirect
import json
import time
import os
from django.core import serializers
#import time,simplejson,json,os,commands

# Create your views here.
def index(request):
    return render(request,'base.html')

#http://127.0.0.1:8082/register
# 0 失败 1 成功 register
def register(req):
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
        dic = req.GET.dict()
        print(dic)
        username = dic['username']
        context=dic['context']
        letter_topic=dic['letter_topic']
        right = dic['right']
        flag = dic['flag']
    # username="lidan"
    # context="这是一个内容文档"
    # letter_topic="0"
    # right="0"
    # flag="0"
    data=[username,context,letter_topic,right,flag]
    save(data)

    return HttpResponse({"status": 200, "msg": "OK", "data":0 })


#http://127.0.0.1:8001/all_message?page=9&letter_topic="爱情"
#信件广场上得到一页6个并且返回所有
    re=1
    return HttpResponse(re)
#http://127.0.0.1:8001/all_message/?page=9

def all_message(req):
    print(req)
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_topic = dic['letter_topic']
        page=dic['page']
        ##有分类的主题
        if letter_topic:
            data_list=get_letter(letter_topic,page)
            data=json.dumps(data_list)

        else:
            data_list=get_all_letter(page)
            data = json.dumps(data_list)
    return HttpResponse(data)

#localhost/all_message/collect_letter
def collect_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username=dic['username']
        insert_collect_letter(username,letter_id)

def delete_collect_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username = dic['username']
        delete_collect_letter_from_table(username, letter_id)

#send_xinli_message?page=1&top=“焦虑症”
def send_xinli_message(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        page = dic['page']
        top = dic['top']
        if top:
            data_list=get_message(top,page)
        else:
            data_list=get_xinli_all_message(page)
    data = json.dumps(data_list)
    return HttpResponse(data)


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

def userlist(req):
    loginbean = req.session['loginbean']
    if loginbean == None:
        return HttpResponse("0")
    rs = User.objects.filter().all()
    jsonArr = serializers.serialize("json", rs)
    return HttpResponse(jsonArr)