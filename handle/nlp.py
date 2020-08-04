#coding=utf-8
import requests
import json
# from urllib import quote
import urllib.parse

def phrase_analyse(context):

  #  text=quote(context)
    text=urllib.parse.quote(context, safe='')
    host1 = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6gNSV8ty03PqBxfv5ll1xHRj&client_secret=WavVBOmQIWsVW9nnbX8NCEeM1TWf6stk'
    host='''https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined?access_token=24.cfd9f6e51c4479b993172c6d012916ed.2592000.1599050847.282335-21774338&text={}'''.format(text)
    response = requests.get(host)

    if response:
        a=response.json()
        #res=json.dumps(a, encoding="UTF-8", ensure_ascii=False)
        if a['conclusion']=="合规":
            check_probability=0
        else:
            check_probability=a['data'][0]['hits'][0]['probability']

        return check_probability

# if __name__=="__main__":
#     print("main")
#     text = "随随便便去死不是一个好傻逼的事情lidan"
#     phrase_analyse(text)