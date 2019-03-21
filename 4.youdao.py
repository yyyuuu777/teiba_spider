#coding:utf-8
import requests
import hashlib
import time
import random
import json


class Youdao(object):

    def __init__(self, word):
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-2079233833@10.169.0.83; JSESSIONID=aaa22JzVLlYBUamMMoEMw; OUTFOX_SEARCH_USER_ID_NCOO=1759572890.208314; ___rl__test__cookies=1553141390616',
            'Referer': 'http://fanyi.youdao.com/?keyfrom=dict2.index'
        }
        self.formdata = None
        self.word = word

    def generate_formdata(self):
        '''
 
            ts": "r = "" + (new Date).getTime()
            salt": "ts + parseInt(10 * Math.random(), 10);
            sign": "n.md5("fanyideskweb" + e + i + "1L5ja}w$puC.v_Kz3@yYn")

        '''
        ts = str(int(time.time()*1000))
        salt = ts + str(random.randint(0, 9))

        tempstr = "fanyideskweb" + self.word + salt + "1L5ja}w$puC.v_Kz3@yYn"
        md5 = hashlib.md5()
        md5.update(tempstr.encode())
        sign = md5.hexdigest()

        self.formdata = {
            "i": self.word,
            "from": "AUTO",
            "to": "AUTO",
            "smartresult": "dict",
            "client": "fanyideskweb",
            "salt": salt,
            "sign": sign,
            "ts": ts,
            "bv": "1091acae250d0ce1bb468d0a7c1b7850",
            "doctype": "json",
            "version": "2.1",
            "keyfrom": "fanyi.web",
            "action": "FY_BY_REALTlME",
            "typoResult": False
        }

    def get_data(self):
        print(self.formdata)
        response = requests.post(self.url, data=self.formdata, headers=self.headers)
        return response.content


    def run(self):
        # url
        # headers
        # formdata
        self.generate_formdata()
        print(self.formdata)
        # 发送请求，获取响应
        data = self.get_data()
        print(data)
        # 解析数据

if __name__ == '__main__':
    youdao = Youdao("人生苦短，及时行乐")
    youdao.run()