#coding=utf-8
from myapp.mysql import connect

def get_message(top,page,username):
    # 比如page=2 那么start就是7开始到12
    page = int(page)
    start = (page - 1) * 4
    end = page * 4
    sql = '''select * from myapp_xinli where  topic="{}" '''.format( top)
    res = connect(sql)
    data_list = []
    for i in res:
        t = {
            "title": i[1],
            "context": i[2],
            "editor": i[3],
            "date": i[4],
            "xinli_id": i[0],
            "url":i[7],
            "collect_flag":0
        }
        data_list.append(t)
    data_list=data_list[start:end]
    xinli_id=i[0]
    sqlcollect = '''select * from myapp_collect_xinli where username="{}" and xinli_id={}'''.format(username,
                                                                                                      xinli_id)
    rescollect = connect(sqlcollect)
    for j in rescollect:
        t["collect_flag"] = 1

    sql2 = '''select count(*) from myapp_xinli where topic="{}" '''.format(top)
    res2 = connect(sql2)

    for i in res2:
        num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list

def get_xinli_all_message(page,username):
    page = int(page)
    start = (page - 1) * 4
    end = page * 4
    sql = '''select * from myapp_xinli '''
    res = connect(sql)
    num=0
    data_list = []
    for i in res:
        t = {
            "title": i[1],
            "context": i[2],
            "editor": i[3],
            "date": i[4],
            "xinli_id": i[0],
            "url": i[7],
            "collect_xinli":0
        }
        xinli_id = i[0]
        sqlcollect = '''select * from myapp_collect_xinli where xinli_id={} and username="{}"'''.format(xinli_id,username)
        rescollect = connect(sqlcollect)
        for j in rescollect:
            t["collect_flag"] = 1
        num=num+1
        data_list.append(t)
    data_list = data_list[start:end]
    # sql2 = '''select count(*) from myapp_letter where  "delete"=0'''
    # res2 = connect(sql2)
    # for i in res2:
    #     num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list


def do_collect_xinli(username,xinli_id):
    letter_id=int(xinli_id)
    sql='''insert into myapp_collect_xinli (username,xinli_id) values("{}",{}) '''.format(username,xinli_id)
    connect(sql)

def delete_collect_xinli_from_table(username,xinli_id):
    letter_id = int(xinli_id)
    sql='''DELETE FROM myapp_collect_xinli WHERE username = "{}" and xinli_id={} '''.format(username,xinli_id)
    connect(sql)

