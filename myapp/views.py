#coding=utf-8

from django.shortcuts import render
from myapp.mysql import connect
from myapp.models import User
from handle.letter import save,get_letter,get_all_letter,insert_collect_letter,delete_collect_letter_from_table,show_all_my_letter
from handle.reply_letter import save_reply_letter,show_reply_letter,show_receive_reply_letter
from handle.xinli import  get_message,get_xinli_all_message,do_collect_xinli,delete_collect_xinli_from_table
from handle.show_all_collect import  show_my_letter_reply_collect,show_xinli_collect
from handle.nlp import phrase_analyse
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
    if req.method == "POST" or req.method == "GET":
        dic = req.GET.dict()
        username = dic['username']
        context=dic['context']
        letter_topic=dic['letter_topic']
        right = int(dic['right'])
        flag = int(dic['flag'])
    # username="lidan"
    # context="这是一个内容文档"
    # letter_topic="0"
    # right="0"
    # flag="0"
    data=[username,context,letter_topic,right,flag]
    save(data)
    dict = {'data': 'save success'}
    data = json.dumps(dict)
    return HttpResponse(data)



#http://127.0.0.1:8001/all_message/?page=9


#广场展示所有的信件内容
def all_message(req):
    print(req)
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_topic = dic['letter_topic']
        username=dic['username']
        page=dic['page']
        ## 去查找
        ##有分类的主题
        if letter_topic:
            data_list=get_letter(letter_topic,page,username)
            data=json.dumps(data_list)
        else:
            data_list=get_all_letter(page,username)
            data = json.dumps(data_list)
    return HttpResponse(data)

#localhost/all_message/collect_letter
def collect_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username=dic['username']
        insert_collect_letter(username,letter_id)
        dict = {'data': 'collect success'}
        data = json.dumps(dict)
    return HttpResponse(data)

def delete_collect_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username = dic['username']
        delete_collect_letter_from_table(username, letter_id)
        dict = {'data': 'delete collect success'}
        data = json.dumps(dict)
    return HttpResponse(data)

#个人中心下的展示
def show_my_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        username = dic['username']
        page = dic['page']
        which_right=dic['which_right']
        data_list=show_all_my_letter(username,page,which_right)
        data = json.dumps(data_list)
    return HttpResponse(data)


# 收藏心理
def collect_xinli(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        xinli_id = dic['xinliID']
        username=dic['username']
        do_collect_xinli(username,xinli_id)
        dict = {'data': ' collect success'}
        data = json.dumps(dict)
    return HttpResponse(data)

def delete_collect_xinli(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        xinli_id = dic['xinliID']
        username = dic['username']
        delete_collect_xinli_from_table(username, xinli_id)
        dict = {'data': 'delete collect success'}
        data = json.dumps(dict)
    return HttpResponse(data)

#send_xinli_message?page=1&top=“焦虑症”
def send_xinli_message(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        page = dic['page']
        top = dic['top']
        username=dic['username']


        if top:
            data_list=get_message(top,page,username)
        else:
            data_list=get_xinli_all_message(page,username)
    data = json.dumps(data_list)
    return HttpResponse(data)

def show_collect(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        username = dic['username']
        collect_type = dic['collect_type']
        do_show_collect(username,collect_type)


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



def get_letter_byID(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        sql='''select * from myapp_letter where id={}'''.format(letter_id)
        res=connect(sql)
        data_list=[]
        for i in res:
            t = {
                "letter_topic": i[4],
                "letterID": i[0],
                "context": i[2],
            }
            data_list.append(t)
    data = json.dumps(data_list)
    return HttpResponse(data)

def reply_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username=dic['username']
        context=dic['context']
        res=phrase_analyse(context)
        #不合格
        if res==1:
            dict = {'data': 'reply success but exist Unqualified words','probability':res}
        #suspect
        if res>=0.5 and res<1:
            dict = {'data': 'reply success but maybe exist Unqualified words', 'probability': res}
        if res<0.5:
            dict = {'data': 'reply success'}
        save_reply_letter(letter_id, username, context, res)


        data = json.dumps(dict)
    return HttpResponse(data)

def get_reply_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        letter_id = dic['letterID']
        username = dic['username']
        page=dic['page']
        dict=show_reply_letter(letter_id,username,page)
    data = json.dumps(dict)
    return HttpResponse(data)

def receive_reply_letter(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        username = dic['username']
        page=dic['page']
        dict=show_receive_reply_letter(username,page)
    data = json.dumps(dict)
    return HttpResponse(data)

def show_my_collect(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        username = dic['username']
        page=dic['page']
        dict = show_my_letter_reply_collect(username, page)
    data = json.dumps(dict)
    return HttpResponse(data)

def show_my_xinli_collect(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        username = dic['username']
        page=dic['page']
        dict = show_xinli_collect(username, page)
    data = json.dumps(dict)
    return HttpResponse(data)

def unread_to_read(req):
    if req.method == "GET" or req.method == "POST":
        dic = req.GET.dict()
        reply_id = dic['reply_id']
        sql = '''UPDATE reply_letter SET read_flag=1 WHERE id={}; '''.format(reply_id)
        connect(sql)
        dict = {'data': 'success'}
        data = json.dumps(dict)
    return HttpResponse(data)


