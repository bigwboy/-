#!/usr/bin/env python
#--*-- coding:utf-8 --*--
#阿呆机器人


import requests
import json
from datetime import datetime

key="004c0a2bffc7482b9b10d3e0edecd95f"



if  __name__=="__main__":
    while True:
        data = str(input('主人：'))
        data = {"key": key, "info": data}
        postdata = json.dumps(data)
        r = requests.post('http://www.tuling123.com/openapi/api', data=postdata)
        rend_data = r.text
        updata = json.loads(rend_data)
        rend_data = ''
        # 根距接收的数据类型选择 say 方式
        if updata['code'] == 100000:
            print('阿呆：'+ updata['text'])
        if updata['code'] == 200000:
            print('阿呆：'+updata['text'])
            print('阿呆：'+updata['url'])
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