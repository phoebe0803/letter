#coding=utf-8
from myapp.mysql import connect
def get_message(top,page):
    # 比如page=2 那么start就是7开始到12
    page = int(page)
    start = (page - 1) * 4
    end = page * 4
    sql = '''select * from myapp_xinli where  topic={} '''.format( top)
    res = connect(sql)
    data_list = []
    for i in res:
        t = {
            "title": i[1],
            "context": i[2],
            "editor": i[3],
            "date": i[4],
            "xinli_id": i[0],
            "url":i[7]
        }
        data_list.append(t)
    data_list=data_list[start:end]
    sql2 = '''select count(*) from myapp_xinli where topic={} '''.format(top)
    res2 = connect(sql2)

    for i in res2:
        num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list

def get_xinli_all_message(page):
    page = int(page)
    start = (page - 1) * 4
    end = page * 4
    sql = '''select * from myapp_xinli where  "delete"=0'''
    res = connect(sql)
    data_list = []
    for i in res:
        t = {
            "title": i[1],
            "context": i[2],
            "editor": i[3],
            "date": i[4],
            "xinli_id": i[0],
            "url": i[7]
        }
        data_list.append(t)
    data_list = data_list[start:end]
    sql2 = '''select count(*) from myapp_letter where  "delete"=0'''
    res2 = connect(sql2)
    for i in res2:
        num = i[0]
    t = {"all_count": num}
    data_list.append(t)
    return data_list