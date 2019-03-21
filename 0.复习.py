# #coding:utf-8
# 反馈
# 网上好多说今年python凉了,真的吗



# #1 什么是爬虫
#     模拟客户端(pc 浏览器 移动端 移动端浏览器/app(使用工具进行抓包/模拟点击操作))，发送网络请求获取对应的相应，并且按照规则自动提取数据的程序
#
# #2 爬虫分类
#     通用爬虫(目标站点没有上限)
#     聚焦爬虫(具体数量的目标站点)
#         功能型爬虫(不采集数据)
#             抢票
#             刷票
#             短信轰炸
#             扫描器
#         数据增量爬虫
#             url 和 数据同时变化的，完整的一条新数据(最多)
#             url不变 数据跟新，更新旧有数据
# #3 http与https的区别
#     ssl
#     性能 https慢
#     安全 https安全
#
# #4 dns服务器的功能
#     域名 ---- ip
#     浏览器会发送所有相关请求获取响应，并且将所有响应进行渲染
#     爬虫只会去发送指定请求，程序员需要仔细分析所有请求，找到能够获取数据的关键其请求进行模拟
#         骨骼
#         js/ajax
#         font/img/css
#
# #6 请求与响应
#     请求
#         User-Agent
#         referer
#         cookies
#         content-length  post 请求体
#     响应
#         Set-Cookies
#
# #8 状态码
#     任何状态码都不可信，一切以浏览器抓包/工具抓包源码为准
#
#
# #10 requests的使用

#     import requests
#
#     # 发送一个简单的请求
#     response = requests.get(url)
#     response = requests.get(url,headers)          一般默认携带UA
#     response = requests.get(url,headers,cookies={})
#     response = requests.get(url,headers,params)       构建参数字典，首先要找到关键参数
#     timeout
#     verify
#     cookiejar_from_dict
#     1. post的用法
#         requests.post(url,data={})
    #         写死
    #         填写
    #         提取
    #             html
    #             发包提取
    #         js运算生成   3 4
#     2. post的使用场景
#         模拟登陆
#         对api接口发送请求
#
#     3. requests如何使用代理
#         proxies= {'http':'http://ip:port','https':'https://ip:port'}
#         proxies= {'http':'http://user:pwd@ip:port','https':'https://user:pwd@ip:port'}
#         requests.get(url,proxies=proxies)
#
        # proxy = random.choice([ip:port,ip1:port1])

#     4. 为什么使用代理
#         分散请求

#     5. session的使用方法
#         创建对象
#          session= requests.session()
#
#          seession.post(url,data={})
