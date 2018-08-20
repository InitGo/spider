#获取个人微信号中朋友信息
#导入itchat包
from itchat.content import *

import itchat





@itchat.msg_register
def simple_reply(msg):
    if msg['Type'] == TEXT:
        return 'I received: %s' % msg['Content']


itchat.auto_login(hotReload=True)
itchat.run()