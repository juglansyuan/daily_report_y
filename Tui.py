import requests


def server_post(Subject, Message, Sckey):
    url = 'https://sctapi.ftqq.com/' + Sckey + '.send'
    d = {'title': Subject, 'desp': Message}
    r = requests.post(url, data=d)

def kutui_post(Subject, Message, Kutui_key):
    url = 'https://push.xuthus.cc/send/' + Kutui_key + '?c=' + Subject + '\n\n' + Message
    r = requests.post(url)
