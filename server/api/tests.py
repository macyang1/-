from django.test import TestCase

# Create your tests here.


import itchat
import time

itchat.auto_login()

friends = itchat.get_friends(update=True)
lenght = len(friends)
yuj = (lenght * 2) / 60
time.sleep(2)
itchat.send(u'为了防止封号2秒检测一位好友哦', 'filehelper')
time.sleep(2)
itchat.send(u'用户数:' + str(lenght) + '人,预计:' + str(yuj) + '分钟', 'filehelper')
time.sleep(2)
for i in range(1, lenght):
    print(friends[i]['NickName'])
    # print(friends[i]['NickName'].encode('utf-8'))
    if friends[i]['UserName'] not in [""]:
        sendstate = itchat.send(
            '自动检测微信僵尸粉程序正在执行中，收到消息的朋友请忽略此消息'
            '，请谅解谢谢~', toUserName=friends[i]['UserName'])

        print(sendstate)
        print(i)
        time.sleep(1)
        if (i % 10 == 0):
            itchat.send(u'已扫描:' + str(i) + '人', 'filehelper')
time.sleep(2)
itchat.send(u'====扫描结束====', 'filehelper')
