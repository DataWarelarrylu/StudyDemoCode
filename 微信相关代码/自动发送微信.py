from wxpy import *
import requests
from threading  import Timer
bot=Bot()
def get_new1():
    url='http://open.iciba.com/dsapi'
    r = requests.get(url)
    contents =r.json()['content']
    translation = r.json()['translation']
    return contents,translation
def send_news():
    try:
        my_friend = bot.friends().search(u'小茅')[0]
        my_friend.send(get_new1()[0])
        my_friend.send(get_new1()[1][:5])
        my_friend.send(u'来自外星人的问候')
        t= Timer(86400,send_news)
        t.start()
    except:
        my_friend = bot.friends().search(u'freedi')[0]
        my_friend.send(u'发送失败')

if __name__ == '__main__':
    send_news()