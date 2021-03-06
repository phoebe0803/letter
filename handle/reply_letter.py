#coding=utf-8
from myapp.mysql import connect

def save_reply_letter(letter_id,username,context,probability):
    sql = '''insert into reply_letter (username,letter_id,reply_context,probability) values("{}",{},"{}","{}") '''.format(username, letter_id,context,probability)
    print(sql)
    connect(sql)

def show_reply_letter(letter_id,username,page):
    page = int(page)
    start = (page - 1) * 6
    end = page * 6
    sql='''select * from reply_letter where letter_id={} and probability<0.5'''.format(letter_id)
    res=connect(sql)
    data_list=[]
    num=0
    ## 每条记录判断这个用户是否有收藏
    for i in res:
        num=num+1
        if i[3]==username:
            collect_flag=i[5]
        else:
            collect_flag=0
        t={
            "id":i[0],
            "reply_context":i[2],
            "collect_flag":collect_flag
        }
        data_list.append(t)
    data_list = data_list[start:end]
    t = {"all_count": num}
    data_list.append(t)
    return data_list

def show_receive_reply_letter(username,page):
    page = int(page)
    start = (page - 1) * 6
    end = page * 6
    sql='''select * from myapp_letter as a left join  reply_letter as b on (b.letter_id=a.id ) where a.username="{}"  and b.probability<0.5 and b.id is not null order by read_flag ASC'''.format(username)
    res=connect(sql)
    data_list=[]
    num=0

    for i in res:
            num = num + 1
            t = {
                "reply_id":i[9],
                "reply_context": i[11],
                "read_flag": i[13],
                "collect_flag":i[14]
            }
            data_list.append(t)
    data_list = data_list[start:end]
    t = {"all_count": num}
    data_list.append(t)
    return data_list



