#coding=utf-8
from myapp.mysql import connect


def do_show_collect(username,collect_type):
    collect_type=int(collect_type)
    #letter
    if collect_type==0:
        sql='''select * from myapp_collect '''
        return 0
    #xinli
    if collect_type==1:
        return 0

def show_my_letter_reply_collect(username,page):
    page = int(page)
    start = (page - 1) * 6
    end = page * 6
    ##找到这个用户收藏的letter_id
    sql1='''select * from myapp_collect_letter where username="{}"'''.format(username)
    res=connect(sql1)
    data_list=[]
    num=0
    for i in res:
        num=num+1
        sql2='''select * from myapp_letter where id={}'''.format(i[2])
        res2=connect(sql2)
        for j in res2:
            t={
                "context":j[2]
            }
            data_list.append(t)
    t = {"all_count": num}
    data_list.append(t)
    return data_list



