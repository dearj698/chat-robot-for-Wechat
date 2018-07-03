from itchat.content import *
import requests
import json
import itchat

itchat.auto_login(hotReload = True)
# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "e5ccc9c7c8834ec3b08940e290ff1559"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])


@itchat.msg_register(itchat.content.TEXT,[TEXT,MAP,CARD,NOTE,SHARING])
def simple_reply(recv_msg):
    msg = recv_msg['Text']
    if recv_msg['User']['NickName']=='女贞陈绍' and '绪儿' in msg:
                itchat.send(msg='收到！ econ姐姐你稍等啊，我来告诉我哥哥',toUserName=recv_msg['FromUserName'])
                itchat.send(msg='哥哥，econ姐姐找你来啦',toUserName='@761fe40be034ff36b87da2d9d2dfa787f7bd56a2b64180ef7cf10c2bece6f5c5')
    if msg == '你是谁啊'or msg=='你是谁'or msg=='你叫什么呀' or msg=='你好':
        itchat.send(msg=u'你好，我的名字是久保史绪里',toUserName=recv_msg['FromUserName'])
    elif msg == '你男朋友是谁'or msg=='你单身吗' or msg=='你有喜欢的人嘛？' or msg=='单身吗' or '喜欢你' in msg:
        if recv_msg['User']['NickName']=='久保栞':
            itchat.send(msg=u'我都知道哦哥哥，这是我和哥哥的小秘密',toUserName=recv_msg['FromUserName'])
        else:
            itchat.send(msg=u'我还是单身哦，但是我有个哥哥，叫Jerry，得问问他同不同意',toUserName=recv_msg['FromUserName'])
    elif '女朋友' in msg:
        itchat.send(msg=u'我得和我哥哥说一下哦',toUserName=recv_msg['FromUserName'])
    elif msg=='绪儿，在吗' or '绪儿' in msg:
        if '乖' in msg:
            itchat.send(msg=u'为了你，我愿意变成你喜欢的样子',toUserName=recv_msg['FromUserName'])
        else:
                itchat.send(msg=u'在的，怎么啦亲',toUserName=recv_msg['FromUserName'])
    elif msg =='在吗' or msg =='在吗在吗':
        itchat.send(msg=u'在的，什么事情啊亲',toUserName=recv_msg['FromUserName'])
    elif '绪儿' in msg or '哪里人' in msg or '出生' in msg:
        itchat.send(msg='我是日本宫城出生的！',toUserName=recv_msg['FromUserName'])
    elif '你' in msg and '父母' in msg:
        itchat.send(msg='我爸爸妈妈在宫城',toUserName=recv_msg['FromUserName'])
    elif '你' in msg and '哪' in msg:
        itchat.send(msg='我在日本东京呀',toUserName=recv_msg['FromUserName'])
    elif 'jerry' in msg or 'Jerry' in msg or '刘钊华' in msg:
        itchat.send(msg=u'emmm,我哥哥啊，怎么啦',toUserName=recv_msg['FromUserName'])
    elif '在干嘛' in msg:
        itchat.send(msg=u'小傻瓜，我在和你聊天呀',toUserName=recv_msg['FromUserName'])
    elif msg=='我是谁' or msg=='我叫什么' or '我是谁'in msg :
        itchat.send(msg='你是'+recv_msg['User']['NickName']+'呀',toUserName=recv_msg['FromUserName'])
    elif msg=='多伦多最火爆的餐厅是哪家':
        itchat.send(msg='我不知道，但是主人说是叫Canoe，你谷歌一下？',toUserName=recv_msg['FromUserName'])
    elif 'em' in msg:
        itchat.send(msg='嗯。。。。',toUserName=recv_msg['FromUserName'])
    elif '66' in msg:
        itchat.send(msg='哈哈哈哈哈',toUserName=recv_msg['FromUserName'])
    elif '233' in msg:
        itchat.send(msg='哈哈哈哈哈',toUserName=recv_msg['FromUserName'])
    elif '姐' in msg:
        itchat.send(msg='怎么啦妞宝',toUserName=recv_msg['FromUserName'])
    elif '在减肥' in msg or '多重' in msg:
        itchat.send(msg='我不告诉你哼😕',toUserName=recv_msg['FromUserName'])


    elif '在干什么' in msg:
        itchat.send(msg='小傻瓜，我在和你聊天呀',toUserName=recv_msg['FromUserName'])
    elif '你' in msg and '在哪儿' in msg:
        itchat.send(msg='我在乃木坂46呀，当然是日本了',toUserName=recv_msg['FromUserName'])
    elif '久保史绪里' in msg or 'ten' in msg:
        itchat.send(msg='叫我干什么啊 我会害羞的',toUserName=recv_msg['FromUserName'])
    else:
        itchat.send('%s' % tuling(recv_msg['Text']),recv_msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])

def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
    # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
    item = group_id(u'吉本坂')  # 根据自己的需求设置
    if msg == '你是谁啊'or msg=='你是谁'or msg=='你叫什么呀' or '你好绪儿' in msg:
            itchat.send(msg=u'你好，我的名字是久保史绪里',toUserName=item)

    itchat.send(u'%s' % tuling(msg['Text']), item)

itchat.run()
