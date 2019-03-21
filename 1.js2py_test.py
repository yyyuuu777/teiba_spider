#coding:utf-8
# pip/pip3 install js2py
import js2py
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36'
}

rsa_js = requests.get('http://s.xnimg.cn/a85738/wap/mobile/wechatLive/js/RSA.js', headers=headers).content.decode()

# print(rsa_js)
# 创建js执行环境对象
context = js2py.EvalJs()

# 将js代码放到执行环境对象中执行
context.execute(rsa_js)

context.t = {"class":"python37"}

print(context.t)
print(type(context.t))