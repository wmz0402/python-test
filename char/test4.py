#初始化变量
from random import choice

answer='y'
while answer=='y':
    print("-----------------------查询功能--------------------------")
    print("1.余额查询。")
    print("2.查询当前剩余流量")
    print("3.查询当前剩余通话时长")
    print("0.退出系统")
    choice = input("请输入您要查询的项目：")
    if choice=='1':
        print("您的余额为：999元")
    elif choice=='2':
        print("剩余流量为：99GB")
    elif choice=='3':
        print("您的剩余通话时长为：999分钟")
    elif choice=='0':
        print("谢谢您的使用！")
        break
    else:
        print("没有该选项！请重新输入")
    answer=input("还要继续操作吗！y/n")
else:
    print("程序退出谢谢您的使用！")

print("---------------------------------------------------")
#九九乘法表
for i in range(1,11):
    for j in range(1,i+1):
        print(str(i)+"*"+str(j)+"="+str(i*j),end='\t')
    print()

print("----------------------------------------------------")
#猜数字，声称随机数
import random
rand = random.randint(1,100)#生成一到一百的一个随机数
count=1#记录猜数的次数
while count<=10:
    number = eval(input("在我心中有一个数字一到一百请猜出他是谁："))
    if number==rand:
        print("恭喜你猜对了！")
        break
    elif number>rand:
        print("猜大了")
    else:
        print("猜小了")
    count+=1
if count<=3:
    print("真聪明，一共猜了",count,"次")
elif count<=6:
    print("还可以一共猜了",count,"次")
else:
    print("猜的次数有点多，一共猜了",count,"次")