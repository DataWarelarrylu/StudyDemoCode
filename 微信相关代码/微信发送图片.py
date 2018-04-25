import itchat
itchat.auto_login(hotReload=True) #热启动你的微信
#itchat.run()
# rooms=itchat.get_chatrooms(update=True)
# for i in range(len(rooms)):
#  print(rooms[i]) #查看你多有的群
room = itchat.search_friends(name=r'冯迪')  # 这里输入你好友的名字或备注。
print(room)
userName = room[0]['UserName']
f = r"//192.168.XX.XXX/tbwxtk/jdyj.png"  # 图片地址
try:
    itchat.send_image(f,toUserName=userName)
    # itchat.send_msg('你好，我是外星人')
    print("success")
except:
    print("fail")