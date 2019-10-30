from numpy import *
import itchat
from threading import Timer

def get_userName():
    itchat.auto_login(hotReload=True)
    friend=itchat.search_friends(name="HongJuan")
    print(friend)
    userName = friend[0]['UserName']
    return userName

def send_msg():
    userName = get_userName()
    itchat.send("Hi~", toUserName=userName)
    t = Timer(3600, send_msg)
    t.start()
send_msg()



