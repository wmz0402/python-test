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


import  admin.my_admin as a   #包名.模块名 admin是包名，my_admin是模块名
a.info()  #__init__.py自动执行

print("-"*40)
#__init__.py只执行一次
from admin import my_admin as b
b.info()
print("-"*40)
#导入具体函数
from admin.my_admin import info
info()
print("-"*40)

