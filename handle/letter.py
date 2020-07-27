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


def get_letter(letter_topic,page,username):
    page=int(page)
    start=(page-1)*6
    end=page*6
    sql = '''select * from myapp_letter where "right"=0 and flag=1 and letter_topic="{}" and "delete"=0'''.format(letter_topic)

    res = connect(sql)
    ## todo sql2
    data_list=[]
    for i in res:
        t={
            "letter_topic":i[4],
            "letterID":i[0],
           "username":i[1],
           "context":i[2],
           "collect_flag":0
           }
        letter_id=i[0]
        sqlcollect = '''select * from myapp_collect_letter where username="{}" and letter_id={}'''.format(username, letter_id)
        rescollect = connect(sqlcollect)
        for j in rescollect:
            t["collect_flag"]=1
        data_list.append(t)
    data_list = data_list[start:end]
    sql2='''select count(*) from myapp_letter where "right"=0 and flag=1 and letter_topic="{}" and "delete"=0'''.format(letter_topic)
    res2 = connect(sql2)
    for i in res2:
        num=i[0]
    t={"all_count":num}
    data_list.append(t)
    return data_list

def get_all_letter(page,username):
    page = int(page)
    start = (page - 1) * 6
    end = page * 6
    sql = '''select * from myapp_letter where "right"=0 and flag=1  and "delete"=0'''
    res = connect(sql)
    data_list = []
    for i in res:
        # 根据letter_id 和username 去myapp_collect 去查找是否有这个记录
        #todo

        t = {
            "letter_topic": i[4],
            "letterID": i[0],
            "username": i[1],
            "context": i[2],
            "collect_flag": 0
        }
        letter_id = i[0]
        sqlcollect = '''select * from myapp_collect_letter where username="{}" and letter_id={}'''.format(username,
                                                                                                          letter_id)
        rescollect = connect(sqlcollect)
        for j in rescollect:
            t["collect_flag"] = 1

        data_list.append(t)
    data_list = data_list[start:end]
    sql2 = '''select count(*) from myapp_letter where "right"=0 and flag=1  and "delete"=0'''
    res2 = connect(sql2)
    for i in res2:
        num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list

def insert_collect_letter(username,letter_id):
    letter_id=int(letter_id)
    sql='''insert into myapp_collect_letter (username,letter_id) values("{}",{}) '''.format(username,letter_id)
    print(sql)
    connect(sql)

def delete_collect_letter_from_table(username,letter_id):
    letter_id = int(letter_id)
    sql=''' delete from myapp_collect_letter 
WHERE username="{}" and letter_id={}'''.format(username,letter_id)
    connect(sql)

def show_all_my_letter(username):
    sql='''select * from myapp_letter where username="{}"'''.format(username)
    res=connect(sql)
    data_list=[]
    for i in res:
        t = {
            "letter_topic": i[4],
            "letterID": i[0],
            "context": i[2],
        }
        data_list.append(t)
    return data_list
