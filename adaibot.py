#!/usr/bin/env python
#--*-- coding:utf-8 --*--
#阿呆机器人


import requests
import json
from datetime import datetime
from bs4 import BeautifulSoup
import os
#图灵机器人key
key="004c0a2bffc7482b9b10d3e0edecd95f"

#百度语音API
baiduapi=""

def botmain():
        data = str(raw_input('主人：'))
        data = SpeakInput()
        data = {"key": key, "info": data}
        postdata = json.dumps(data)
        r = requests.post('http://www.tuling123.com/openapi/api', data=postdata)
        rend_data = r.text
        updata = json.loads(rend_data)
        rend_data = ''
        # 根距接收的数据类型选择 say 方式
        if updata['code'] == 100000:
            test=updata['text'].encode('utf-8')
            TextToAdieo(test)
            print('阿呆：'+ updata['text'].encode('utf-8'))
        if updata['code'] == 200000:
            test1 = updata['text'].encode('utf-8')
            TextToAdieo(test1)
            print('阿呆：'+updata['text'].encode('utf-8'))
            print('阿呆：'+updata['url'].encode('utf-8'))
            test2 = updata['url'].encode('utf-8')
            TextToAdieo(test2)
        if updata['code'] == 308000:
            temp = (updata['list'])
            for i in range(0, len(temp)):
                client_data = dict(temp[i])
                print(client_data['icon'])
                print(client_data['name'])
                print(client_data['info'])
                print(client_data['detailurl'])
        if updata['code'] == 302000:
            temp = (updata['list'])
            for i in range(0, len(temp)):
                client_data = dict(temp[i])
                print(client_data['article'])
                print(client_data['icon'])
                print(client_data['source'])
                print(client_data['detailurl'])



def TextToAdieo(text):
    url = u'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_' \
          u'demo&cod=2&lan=zh&ctp=1&pdt=1&spd=4&per=4&vol=5&pit=5'.format(text)
    os.system('mplayer "%s"' % url)

def AdieoToText(Adieo):
    os.system()
    return Text

def SpeakInput():

    return text


if  __name__=="__main__":
    while True:
        botmain()