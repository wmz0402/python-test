#查询python中的保留字
import keyword
print(keyword.kwlist) #关键字列表
print(len(keyword.kwlist)) #计算保留字的总个数

#变量的定义和使用
luck_number = 8
my_name = "luck007"
print(luck_number,"的数据类型是：",type(luck_number))

#python动态修改变量的数据类型，痛过赋不同类型的值就可以直接修改
luck_number = "luck007"
print("现在的数据类型是",type(luck_number))

#python中允许多个变量指向同一个值
no = number = 1024
print(no,number)
print(id(no),id(number)) #id()函数用来查看变量的内存地址

#整数不同的表示形式
num = 123
num1 = 0b101010 #使用二进制表示
num2 = 0o765  #使用八进制表示
num3 = 0x87ABF #使用十六进制表示
print(num1,num2,num3)

#小数
x = 1.99E1413
print("科学计数法",x,"数据类型：",type(x))
print(0.1 + 0.2)  #会出现不确定的尾数问题

print(round(0.1 + 0.2,1)) #使用round函数可以保留小数

#复数的表示
n = 123 + 456j
print("实数部分：",n.real)
print("虚数部分",n.imag)

#字符串的索引和切片
s = "HELLOWORLD"
print(s[0],s[-10])
print("北京欢迎你"[4])
print("北京欢迎你"[-1])
print("----------------------------------")
print(s[2:7])  #从2开始到7结束不包括7 正向传递
print(s[-8:-3])   #反向递减
print(s[:5])  #默认从零开始到五结束不包含五

#字符串的运算
y="2022年"
z="北京"
print(y+z) #字符串加法可以将两个字符串连接起来
print(y*10)  #字符串乘法表示这个字符串重复几次
print("北京" in z)  #x in y如果x是y的子串会输出True否则是False
print("上海" in z)

#布尔值
#所有非零整数的布尔值都是True
#所有非空字符串的布尔值都是True

#eval函数的使用  就是去掉左右两边的引号
a = "3.14+3"
print(a,type(a))
b = eval(a)
print(b,type(b))

#eval通常和input连用，来获取用户输入的数值
age = eval(input("请输入你的年龄："))
print(age,type(age))

hello = "北京欢迎你！"
print(hello)
print(eval("hello"))   #去掉引号之后是一个变量hello输出这个变量的值


#python支持链式赋值
d=f=g=100
print(d,f,g)

#pyhton支持解包赋值
d,f=1,2
print(d,f)


print("------------------如何交换两个变量的值？（利用系列解包赋值）--------------------------")
d,f = f,d
print(d,f)

print("---------------输出一个四位数各个位置上的数------------------")
n_um=eval(input("请输入一个四位数："))
print("个位数是：",n_um%10)
print("十位数是：",n_um//10%10)
print("百位数是：",n_um//100%10)
print("千位数是：",n_um//1000)
print("-"*20)

n_um1=input("请输入一个四位数")
print("个位数是：",n_um1[3])
print("十位数是：",n_um1[2])
print("百位数是：",n_um1[1])
print("千位数是：",n_um1[0])







