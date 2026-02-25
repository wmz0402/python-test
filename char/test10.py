# #直接导入
# import my_info
# print(my_info.name)
# my_info.info()
#
# #起别名导入
# import my_info as a
# print(a.name)
# a.info()
#
# #导入模块中具体的变量
# from my_info import name
# print(name)
#
# #通配符 导入模块当中的所有
# from my_info import *
# print(name)
# info()
#
# #同时导入多个模块
# import time,math,random

#
# from introduce import *
# from my_info import *
# #导入模块中具有同名的变量和函数，后倒入的会将之前导入的覆盖
# info()
#
# #如果不想覆盖，解决方法，可以使用import
# import my_info
# import introduce
# #使用模块中的函数或变量时，模块名打点调用
# my_info.info()
# introduce.info()
#


# import  admin.my_admin as a   #包名.模块名 admin是包名，my_admin是模块名
# a.info()  #__init__.py自动执行
#
# print("-"*40)
# #__init__.py只执行一次
# from admin import my_admin as b
# b.info()
# print("-"*40)
# #导入具体函数
# from admin.my_admin import info
# info()
# print("-"*40)
#



# #random模块的使用
# import random
# random.seed(10)
# print(random.random()) #[0.0,1.0)
# print(random.random())
# print("-"*30)
# random.seed(10)
# print(random.randint(1,100))
#
#
# for i in range(10):
#     print(random.randrange(1,10,3))
#
# print(random.uniform(1,100))#[a,b]随即小数
#
# lst=[i for i in range(1,11)]
# print(random.choice(lst)) #lst是列表，称为序列
# #随机的排序
# random.shuffle(lst)
# print(lst)


# #time模块的使用
# import time
# now=time.time()
# print(now)
#
# obj=time.localtime() #struct_time对象
# print(obj)
#
# obj2=time.localtime(60)
# print(obj2)
# print(type(obj2))
# print("年份：",obj2.tm_year)
# print("月份：",obj2.tm_mon)
# print("日期：",obj2.tm_mday)
# print("时：",obj2.tm_hour)
# print("分：",obj2.tm_min)
# print("秒：",obj2.tm_sec)
# print("星期：",obj2.tm_wday)
# print("是今年的多少天：",obj2.tm_yday)
# print(time.ctime())  #时间戳对应的易读的字符串
#
# #日期时间格式化
# print(time.strftime("%Y-%m-%d",time.localtime()))
#
# print(time.strftime("%H:%M:%S",time.localtime()))
# print(time.strftime("%B月份名称",time.localtime()))
# print(time.strftime("%A星期名称",time.localtime()))
# #字符串转成struct_time
# print(time.strptime("2008-08-08","%Y-%m-%d"))
# time.sleep(5)
# print("hello world")

# #datetime模块的使用
# #datetime类的使用
# from datetime import datetime  #从datetime模块中导入datetime类
# dt = datetime.now()
# print(dt)
#
# dt2=datetime(2028,8,8,20,8)
# print("dt2的数据类型",type(dt2),"dt2所表示的日期时间：",dt2)
# print("年：",dt2.year,"月：",dt2.day,"日：",dt2.day)
# print("时：",dt2.hour,"分：",dt2.minute,"秒：",dt2.second)
# #比较大小奥
# labor_day=datetime(2028,5,1,20,8)
# national_day=datetime(2028,10,1,20,8)
# print("2028年5.1比10.1要早吗",labor_day<national_day)
#
# #daterime类型与字符串进行转换
# nowdt=datetime.now()
# nowdt_str=nowdt.strftime("%Y/%m/%d %H:%M:%S")
# print("nowdt的数据类型：",type(nowdt),"数据是什么：",nowdt)
# print("nowdt_str:",type(nowdt_str),"nowdt_str:",nowdt_str)\
#
#
# #字符串雷星转成datetime类型
# str_datetime="2028年8月8日 20点8分"
# dt3=datetime.strptime(str_datetime,"%Y年%m月%d日 %H点%M分")
# print(type(str_datetime),str_datetime)
# print(type(dt3),dt3)
# print("-"*50)
# #timedelta类的使用
# from datetime import datetime
# from datetime import timedelta
# #创建两个daterime对象
# delta1=datetime(2028,10,1)-datetime(2028,5,1)
# print(type(delta1),delta1)
# print(datetime(2028,5,1)+delta1)
# #通过传入参数的方法创建一个timedelta对象
# td1=timedelta(10)
# print("创建一个10天的timedelta对象",td1)
# td2=timedelta(10,11)
# print("创建一个10天11秒的timedelta对象",td2)

# #爬取景区天气预报
# import requests
# import re
# url="https://www.weather.com.cn/weather1d/101010200.shtml"#爬虫打开浏览器上的网页
# resp=requests.get(url) #打开浏览器并打开网址
# #设置编码格式
# resp.encoding="utf-8"
# print(resp.text) #resp响应对象，对象名.属性名
#
# city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>', resp.text)
# weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>', resp.text)
# wd = re.findall('<span class="wd">(.*)</span>', resp.text)
# zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>', resp.text)
# # print(city)
#
# lst=[]
# for a,b,c,d in zip(city,weather,wd, zs):
#     lst.append([a,b,c,d])
# print(lst)
# for item in lst:
#     print(item)

# #爬取百度logo
# import requests
# url="https://www.baidu.com/img/PCtm_d9c8750bed0b3c7d089fa7d55720d6cf.png"
# resp=requests.get(url)
# #保存到本地
# with open("logo.png","wb")as file:
#     file.write(resp.content)


# #从pdf文件中提取数据
# import pdfplumber
# #打开pdf文件
# with pdfplumber.open("高数A1自测题4.pdf") as pdf:
#     for i in pdf.pages:
#         print(i.extract_text()) #提取内容
#         print(f"----------------------------第{i.page_number}页结束")

# #对图像进行灰度处理
# #Numpy模块
# import  numpy as np
# import matplotlib.pyplot as plt
# #读取图片
# n1=plt.imread("iphone1.jpg")
# print(type(n1),n1) #数组，三维数组，最高维度表示的是图像的高，次高纬度表示的是图像的宽，最低维度颜色
# plt.imshow(n1)
#
# #编写一个灰度的公式
# n2=np.array([0.29,0.587,0.114]) #创建数组
# #将数组n1颜色值与数组n2进行点乘运算
# x=np.dot(n1,n2)
# #传入数组，显示灰度
# plt.imshow(x,cmap="gray")
# #显示图像
# plt.show()



# #Pandas和Matplotlib模块
# import pandas as pd
# import matplotlib.pyplot as plt


# #饼状图
# from pyecharts import options as opts
# from pyecharts.charts import Pie
# from pyecharts.faker import Faker
#
# # --- 新增下面这两行代码 ---
# from pyecharts.globals import CurrentConfig
# CurrentConfig.ONLINE_HOST = "https://cdn.staticfile.net/echarts/5.4.2/"
# # ---------------------------
#
# # 准备数据 (下面的代码基本保持不变)
# lst = [["华为", 1000], ["OPPO", 1200], ["苹果", 300], ["小米", 980]]
# c = (
#     Pie()
#     # 注意这里顺手帮你加了个参数名 data_pair=，这样写更标准，不容易报错
#     .add(series_name="", data_pair=lst)
#     .set_global_opts(title_opts=opts.TitleOpts(title="2028年北京手机出库占比情况"))
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}%"))
#     .render("phone.html")
# )




# #PIL  颜色交换
# from PIL import Image
# #加载图片
# im=Image.open('iphone1.jpg')
# #提取RGB图像的颜色通道，返回结果试图向副本
# r,g,b=im.split()
# #合并通道
# om=Image.merge(mode='RGB',bands=(r,b,g))
# om.save('test.png')
#


#jieba 对中文进行分词的模块

# #实战一  订票系统
# import prettytable as pt
# from numpy.ma.core import choose
#
#
# #显示坐席
# def show_ticket(row_num):
#     tb=pt.PrettyTable() #创建一张表格
#     #设置标题（表格的排头部分）
#     tb.field_names=["行号","座位1","座位2","座位3","座位4","座位5"]
#     #遍历有票
#     for i in range(1,row_num+1):
#         lst=[f"第{i}行","有票","有票","有票","有票","有票"]
#         tb.add_row(lst)
#     print(tb)
#
# #订票
# def order_ticket(row_num,row,column):
#     tb = pt.PrettyTable()  #创建一张表单
#     tb.field_names = ["行号","座位1","座位2","座位3","座位4","座位5"]
#     for i in range(1,row_num+1):
#         if int(row)==i:
#             lst=[f"第{i}行","有票","有票","有票","有票","有票"]
#             lst[int(column)]="已售"
#             tb.add_row(lst)
#         else:
#             lst = [f"第{i}行", "有票", "有票", "有票", "有票", "有票"]
#             tb.add_row(lst)
#     print(tb)
#
#
# if __name__ == '__main__':
#     row_num=6
#     show_ticket(row_num)
# #开始售票
#     choose_num=input("请输入您选择的坐席：如4,3表示四排三列")
#     row,column=choose_num.split(",")
#     order_ticket(row_num,row,column)
#



#实战二 推算几天后的日期
import datetime
#输入日期
def input_date():
    inputdate=input("请输入开始日期：（20201001）输完后请按回车")
    datestr=inputdate[0:4]+"-"+inputdate[4:6]+"-"+inputdate[6:8]
    #类型转换
    dt=datetime.datetime.strptime(datestr,"%Y-%m-%d")
    return dt


if __name__=="__main__":
    # print(input_date())
    date=input_date()
    # 输入间隔天数
    in_num = eval(input("请输入间隔天数："))
    date=date+datetime.timedelta(days=in_num)
    print("您推算的日期是：",date)













