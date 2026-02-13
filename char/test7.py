#raise关键字的使用
# try:
#     gender=input("请输入您的性别：")
#     if gender!="男"and gender!="女":
#         raise Exception("性别只能是男或女")
#     else:
#         print("您的性别是：",gender)
# except Exception as e:
#     print(e)

#Python 中常见的异常类型

#ZeroDivisionError 当除数为0时，引发的异常
# print(10/0)


#IndexError 索引超出范围引发的异常
# lst=[10,20,30,40]
# print(lst[4])


#KeyError 字典取值时key不存在的异常
# d={"name":"ysj","age":20}
# print(d["gender"])

#NameError 使用一个没有声明的变量时引发的异常
# print(hello)


#SyntsxError Python中的语法错误
# print("hello)

#ValueError 传入的值错误
# print(int("a"))


#AttributeError 属性或方法不存在的异常
# i=10
# print(i.name)


#TypeError 类型不合适引发的异常
# print("hello"+123)

#IndentationError 不正确的缩进引发的异常
    # print("hello world")


 #编写程序接受用户输入的分数信息
# try:
#      score=eval(input("请输入分数："))
#      if 0<=score<=100:
#          print("您的分数是：",score)
#      else:
#          raise Exception("分数不正确")
# except Exception as e:
#      print(e)

#编写程序实现组成三角形的判断
try:
    a=int(input("请输入第一条边："))
    b=int(input("请输入第二条边："))
    c=int(input("请输入第三条边："))
    if a+b>c and a+c>b and b+c>a:
        print("三角形边长为：",a,b,c)
    else:
        raise Exception(f"{a},{b},{c}不能构成三角形")
except Exception as e:
    print(e)














