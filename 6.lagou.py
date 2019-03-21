#coding:utf-8
import requests
import json
import jsonpath

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
response = requests.get(url, headers=headers)
print(response.content)

dict_data = json.loads(response.content)

print(jsonpath.jsonpath(dict_data,'$..name'))

