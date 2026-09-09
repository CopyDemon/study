"""
目的：
爬取CNN恐惧与贪婪指数的脚本。

包的选择：
客户端渲染内容使用到JS 所以python request 无法获取到内容
需要使用playwright 或者 selenium 获取内容
"""

import requests
import json

fear_index_url = "https://www.cnn.com/markets/fear-and-greed"
header = {"User-Agent": "Mozilla/5.0"}

request_result = requests.get(fear_index_url, headers=header, timeout=5000)

print(request_result.text)
