#coding:utf-8
from lxml import etree
import requests
import os
# import sys

class Tieba(object):

    def __init__(self, name):
        self.name = name
        self.url = 'http://tieba.baidu.com/f?kw={}'.format(self.name)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            # 'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt)'
        }

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content

    def parse_list_page(self, page):

        page = page.decode().replace('<!--','').replace('-->','')

        html = etree.HTML(page)

        el_list = html.xpath('//li[@class=" j_thread_list clearfix"]/div/div[2]/div[1]/div[1]/a')

        # print(len(el_list))
        data_list = []

        for el in el_list:
            temp = {}
            temp['title'] = el.xpath('./text()')[0]
            temp['link'] = 'http://tieba.baidu.com' + el.xpath('./@href')[0]
            data_list.append(temp)

        # 提取下一页链接
        try:
            next_url = 'https:' + html.xpath('//a[text()="下一页>"]/@href')[0]
        except:
            next_url = None

        return data_list,next_url

    def parse_detail_page(self, page):

        html = etree.HTML(page)

        image_list = html.xpath('//*[contains(@id,"post_content_")]/img/@src')

        return image_list

    def download(self, image_list):
        if not os.path.exists('image'):
            os.makedirs('image')

        for url in image_list:
            if 'emoticon' in url:
                continue
            data = self.get_data(url)

            filename = 'image' + os.sep + url.split('/')[-1]
            with open(filename,'wb')as f:
                f.write(data)

    def run(self):
        # url
        # headers
        next_url = self.url
        while True:
            # 发送帖子列表页面请求获取响应
            list_page = self.get_data(next_url)

            # 解析响应 提取详情标题与链接列表 & 下一页url
            detail_list, next_url = self.parse_list_page(list_page)

            # 遍历链接列表，发起针对详情页面的请求，获取响应
            for detail in detail_list:

                detail_page = self.get_data(detail['link'])

                # 从响应中提取图片地址
                image_list = self.parse_detail_page(detail_page)
                print(image_list)
                # 下载图片
                self.download(image_list)
            # 翻页

            if next_url == None:
                break

if __name__ == '__main__':
    tieba = Tieba("无耻之徒")
    tieba.run()