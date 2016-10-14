# -*- coding: utf-8 -*-

import requests
import json
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from websocket import create_connection

ws = create_connection("ws://www.opdev.cn/ws/public?subscribe-broadcast&publish-broadcast&echo")
log = file('/data/www/simblog/logs/chat.log', 'a+')



while True:
    receive =  ws.recv()
    if receive != '--heartbeat--':
        receive = json.loads(receive)
        # 不回复机器人自己的消息
        if receive['username'] == u'Robot':
            pass
        elif receive['username'] == u'admin':
            ws.send(json.dumps({"username": "Robot", "message": '你好啊，我是opdev.cn的机器人哦。。。'}))
        else:
            result = requests.post('http://www.tuling123.com/openapi/api', data={'key': 'f9d08d45df864f6093064e9aefd3a135', 'info':receive['message']})
            message = json.loads(result.text)
            ws.send(json.dumps({"username": "Robot", "message": message['text']}))
            # 记录消息日志
            now_time = time.strftime("%Y-%m-%d %X",time.localtime())
            data = '%s username:[%s] receive:[%s] send:[%s]\n'%(now_time, receive['username'] ,receive['message'].decode('unicode_escape'), message['text'])
            print data
            log.write(data)
            log.flush()
ws.close()
log.close()
