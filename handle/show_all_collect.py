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

