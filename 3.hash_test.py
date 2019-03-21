#coding:utf-8
import hashlib

data = 'python87'
# data = 'https://hz.58.com/hezu/37458876695940x.shtml?fzbref=0&from=1-list-0&psid=179253225203573162101108972&iuType=gz_2&ClickID=2&apptype=0&key=&entinfo=37458876695940_0&params=rankhzpriceanxuan0099^desc&cookie=|||c5/njVyTCP4vP5%20xAxmaAg==&PGTID=0d30000a-0004-fef7-555a-bacbcd534f84&pubid=64852275&trackkey=37458876695940_405c9797-d629-4867-844c-e0300b87f6b7_20190321114613_1553139973236&fcinfotype=gz'

# 创建hash对象
md5 = hashlib.md5()

# 向hash对象中添加需要做hash运算的字符串
md5.update(data.encode())

# 获取字符串的hash值
result = md5.hexdigest()

print(result)