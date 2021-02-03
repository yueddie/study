# -*- coding: utf-8 -*-

__author__ = 'eddie'

import urllib.request
import urllib.parse
import urllib.error

# 获取get请求
# data = bytes(urllib.parse.urlencode({"hello": "word", "name": "eddie"}), encoding="utf-8")
# respones = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(respones.read().decode('utf-8'))


# try:
#     respones = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(respones.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print(e)


# respones = urllib.request.urlopen("http://www.baidu.com")
# print(respones.getheader("Server"))


# 请求链接
# url = "http://httpbin.org/post"
# 请求头文件信息
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
# }
# # 请求数据
# data = bytes(urllib.parse.urlencode({"name": "eddie"}), encoding="utf-8")
# # 请求指令
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

url = "http://www.douban.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=headers, method="GET")
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
