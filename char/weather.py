#爬取景区天气预报
import requests
import re

#定义函数
def get_html():
    url = "https://www.weather.com.cn/weather1d/101010200.shtml"  # 爬虫打开浏览器上的网页
    resp = requests.get(url)  # 打开浏览器并打开网址
    # 设置编码格式
    resp.encoding = "utf-8"
    return resp.text  # resp响应对象，对象名.属性名
def parse_html(html_str):
    city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', html_str)
    weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', html_str)
    wd = re.findall('<span class="wd">(.*)</span>', html_str)
    zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', html_str)
    # print(city)
    lst = []
    for a, b, c, d in zip(city, weather, wd, zs):
        lst.append([a, b, c, d])
    return lst




