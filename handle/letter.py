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
def get_letter(letter_topic,page):
    #比如page=2 那么start就是7开始到12
    page=int(page)
    start=(page-1)*6
    end=page*6
    sql = '''select * from myapp_letter where "right"=1 and flag=1 and letter_topic={} and id>{} and id <={} and "delete"=0'''.format(letter_topic,start,end)
    res = connect(sql)
    data_list=[]
    for i in res:
        t={
            "letter_topic":i[4],
            "letterID":i[0],
           "username":i[1],
           "context":i[2],
           "collect_flag":0
           }
        data_list.append(t)
    sql2='''select count(*) from myapp_letter where "right"=1 and flag=1 and letter_topic={} and "delete"=0'''.format(letter_topic)
    res2 = connect(sql2)
    for i in res2:
        num=i[0]
    t={"all_count":num}
    data_list.append(t)
    return data_list

def get_all_letter(page):
    page = int(page)
    start = (page - 1) * 6
    end = page * 6
    sql = '''select * from myapp_letter where "right"=1 and flag=1 and id>{} and id <={} and "delete"=0'''.format( start, end)
    res = connect(sql)
    data_list = []
    for i in res:
        t = {
            "letter_topic": i[4],
            "letterID": i[0],
            "username": i[1],
            "context": i[2],
            "collect_flag": 0
        }
        data_list.append(t)
    sql2 = '''select count(*) from myapp_letter where "right"=1 and flag=1  and "delete"=0'''
    res2 = connect(sql2)
    for i in res2:
        num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list

def insert_collect_letter(username,letter_id):
    letter_id=int(letter_id)
    sql='''insert into myapp_collect (username,letter_id) values({},{}) '''.format(username,letter_id)
    connect(sql)

def delete_collect_letter_from_table(username,letter_id):
    letter_id = int(letter_id)
    sql='''DELETE FROM myapp_collect WHERE username = {} and letter_id={} '''.format(username,letter_id)
