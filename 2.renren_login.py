#coding:utf-8
import requests
import js2py
import json


def login():
    # 创建session对象
    session = requests.session()

    # 设置请求头
    session.headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
    }
    # 发送获取公钥数据包的get请求
    response = session.get('http://activity.renren.com/livecell/rKey')
    # print(response.content)

    # 创建n
    n = json.loads(response.content)['data']

    # 创建t
    t = {
        'password':'!QAZ2wsx#EDC'
    }

    # 获取前置 js代码
    rsa_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js').content.decode()
    bigint_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/BigInt.js').content.decode()
    barrett_js = session.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/Barrett.js').content.decode()

    # 创建js环境对象
    context = js2py.EvalJs()

    # 将变量和js代码加载到环境对象中执行
    context.execute(rsa_js)
    context.execute(bigint_js)
    context.execute(barrett_js)
    context.n = n
    context.t = t

    # 将关键js代码放到环境对象中执行
    pwd_js = """
        t.password = t.password.split("").reverse().join(""),
        setMaxDigits(130);
        var o = new RSAKeyPair(n.e,"",n.n)
          , r = encryptedString(o, t.password);
    """
    context.execute(pwd_js)
    # 获取加密密码
    # print(context.r)


    # 构建formdata
    formdata = {
        "phoneNum": "17173805860",
        "password": context.r,
        "c1": -100,
        "rKey": n['rkey']
    }
    print(formdata)
    # 发送post请求，模拟登陆
    response = session.post('http://activity.renren.com/livecell/ajax/clog', data=formdata)

    # 验证
    print(response.content.decode())


if __name__ == '__main__':
    login()



