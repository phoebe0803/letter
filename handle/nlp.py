#coding=utf-8
import requests
import json
# from urllib import quote
import urllib.parse

def phrase_analyse(context):

  #  text=quote(context)
    text=urllib.parse.quote(context, safe='')
    #host1 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6gNSV8ty03PqBxfv5ll1xHRj&client_secret=WavVBOmQIWsVW9nnbX8NCEeM1TWf6stk'
    host='''https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token=24.cfd9f6e51c4479b993172c6d012916ed.2592000.1599050847.282335-21774338&text={}'''.format(text)
    response = requests.get(host)

    if response:
        a=response.json()
        # res=json.dumps(a, encoding="UTF-8", ensure_ascii=False)
        # print(res)
        if a['conclusion']=="合规"  :
            check_probability=0
        if a['conclusion']=="疑似" and a['data'][0]['hits'][0]['words'] :
            check_probability=a['data'][0]['hits'][0]['probability']
        if a['conclusion']=="不合格":
            check_probability=a['data'][0]['hits'][0]['probability']

        return check_probability


if __name__=="__main__":
    print("main")
    text = "展信佳：不知道能不能收到我写的信。但还是想试试。我从小就是那种乖乖的孩子，老师眼里的好学生，同学眼中的小淑女。我去年参加了高考，现在大一。但好像也是从高考开始，我忽然觉得很无能为力，人人都说大学生活很美好，但我上了大学之后感受到了前所未有的惶恐和焦虑，以前老师讲的课只要我愿意，我可以听懂所有，但是上了大学之后我发现好多课都变得似懂非懂，老师好像也没有以前那么和蔼可亲，我怕挂科，怕扣学分，怕不会顺利"

    print(phrase_analyse(text))