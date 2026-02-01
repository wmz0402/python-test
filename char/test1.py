#输出语句练习
a = 10
b = 20
print(a,b,"sddf")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(chr(98))  #chr()函数会把数字先转换成字符在输出

print(ord("北"))  #ord()函数会把里面的字符转换成Unicode值输出
print(ord("京"))
print(chr(21271))
print(chr(20140))

#使用print函数将内容输入到文件
fp = open("note.txt" , "w")
print("北京欢迎你！",file=fp)
fp.close()

#多行print函数输出一行显示
print("北京",end="-->")
print("欢迎你")

#使用连接符连接字符串
print("北京欢迎你"+"2026") #只能字符串和字符串相连
