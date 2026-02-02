#if多分枝语句
from unittest import case

score = eval(input("请输入你的成绩："))
if score < 0 or score > 100:
    print("你的成绩有误！")
elif 0 <= score < 60:
    print("E")
elif 60 <= score < 70 :
    print("D")
elif 70 <= score < 80 :
    print("C")
elif 80 <= score < 90 :
    print("B")
elif 90 <= score < 100 :
    print("A")

#if语句的嵌套
answer = input("您喝酒了吗？")
if answer == "y":
    proof = eval(input("您的酒精含量："))
    if proof <= 20:
        print("不构成酒驾，一路平安！")
    elif proof < 60:
        print("构成酒驾，请不要开车！")
    else:
        print("已构成醉驾，请不要开车")
else:
    print("没你啥事，你走吧！")


#match - case 结构
Score = input("请输入你的等级：")
match Score:
    case "A":
        print("优秀")
    case "B":
        print("良好")
    case "C":
        print("中等")
    case "D":
        print("及格")
    case "E":
        print("不及格")


#遍历字符串
for i in "hello":
    print(i)

#range()函数，取出一个包含n但不包含m的整数序列[n,m)
for i in range(1,11):
    print(i)

#100到999之间的水仙花数有哪些写
for i in range(100,1000):
    ge=i%10
    sh=i//10%10
    ba=i//100
    if ge**3+sh**3+ba**3 == i:
        print(i)


su = 0
for i in range(1,11):
    su += i
else:
    print(su)


#while无限循环
i = 1
s = 0
while i <= 10:
    s += i
    i += 1
else:
    print(s)


#密码登录验证
i = 0
while i < 3:
    user = input("请输入用户名：")
    psd = input("请输入密码：")
    if user == "luck007" and psd == "0402":
        print("登陆成功！")
        i = 8
    else:
        if i < 2:
            print("还剩",2-i,"次机会")
        i = i+1

if i == 3:
    print("三次机会已用完！")



#输出一个三行四列的长方形
for i in range(1,4):
    for j in range(1,5):
        print("*",end=" ")
    print()
print("-----------------------------")
#打印一个直角三角形
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print("------------------------------------")
#打印倒三角行
for i in range(1,6):
    for j in range(i,7-1):
        print("*",end=" ")
    print()
print("--------------------------------")
#打印正三角形
for i in range(1,6):
    for j in range(1,6-i):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
print("---------------------------------")
#打印菱形实心的
row=eval(input("请输入总长度"))
while row%2==0:
    print("长度不能是偶数，请重新输入")
    row=eval(input("请输入新的长度："))
top_row = (row+1)//2
bottom_row = (row-1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,2*bottom_row-i*2+2):
        print("*",end="")
    print()

print("------------------------------------------")
#打印空心菱形
row = eval(input("请输入总长度："))
while row%2==0:
    print("不能是偶数！")
    row=eval(input("请重新输入："))
top_row = (row+1)//2
bottom_row = (row-1)//2
for i in range(1,top_row+1):
    for j in range(1,top_row-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
for i in range(1,bottom_row+1):
    for j in range(1,i+1):
        print(" ",end="")
    for j in range(1,2*bottom_row-i*2+2):
        if j==1 or j==2*bottom_row-i*2+1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
