#字符串的相关处理方法
from shlex import join

s1='HelloWorld'
new_s2=s1.lower()
print(new_s2,s1)

new_s3=s1.upper()
print(new_s3)
#字符串的分割
e_mail='ysj@126.com'
lst=e_mail.split('@')
print("邮箱名：",lst[0],"邮件服务域名：",lst[1])

print(s1.count('o'))
print(s1.find('o'))
print(s1.index('o'))
print(s1.find('p'))

#判断前后缀
print("demo.py".endswith('py'))
print(s1.startswith('H'))
print(s1.startswith('P'))

s='HelloWorld'
new_s=s.replace('o','你好',1) #默认为全部替换 第三个数据代表替换的个数
print(new_s)
#字符串在指定范围内居中
print(s.center(20))
print(s.center(20,"*"))
#去掉字符串左右的空格
s='      Hello     World      '
print(s.strip()) #去掉左右的
print(s.lstrip()) #去除左侧的
print(s.rstrip()) #去除右侧的

#去掉指定的字符
s3='dl-Helloworld'
print(s3.strip('ld'))
#只要是包含ld当中的字符就会去除和顺序无关
print(s3.rstrip('ld'))
print(s3.lstrip('ld'))

#占位符进行格式化
name="马冬梅"
age=18
score=98.5
print("姓名：%s,年龄：%d,成绩：%.1f"%(name,age,score))

#f-string
print(f'姓名：{name},年龄：{age},成绩:{score}')

#使用字符串的format方法
print('姓名：{0},年龄：{1},成绩：{2}'.format(name,age,score))

s='helloworld'
print("{0:*<20}".format(s))  #字符串的显示宽度为20，左对齐，空白表部分用星号填充
print("{0:*>20}".format(s))
print("{0:*^20}".format(s))

print(s.center(20,"*"))

#千位分隔符，只适用于整数和浮点数
print("{0:,}".format(789654123))
print("{0:,}".format(789654123.12584125))

print("{0:.2f}".format(3.1415926535))  #保留几位小数
print("{0:.5}".format("helloworld"))  #最大显示长度

a=425
print("二进制{0:b},十进制{0:d},八进制{0:o},十六进制{0:x}".format(a))
b=3.1415926
print("{0:.2f},{0:.2E},{0:.2e},{0:.2%}".format(b))

s="伟大的中国梦"
#编码
scode=s.encode(errors='replace')   #默认是utf-8，中文占3个字节
print(scode)

scode_gbk=s.encode("gbk",errors='replace') #gbk中文占2字节
print(scode_gbk)

print(bytes.decode(scode_gbk,'gbk'))

#字符串的拼接
#直接使用加号进行拼接
#使用字符串的join方法
s1='hello'
s2='world'
print("".join([s1,s2]))#使用空字符串进行拼接

print("*".join([s1,s2]))#使用*进行拼接
#使用格式化字符串进行拼接
print("%s%s" % (s1,s2))
print(f"{s1}{s2}")
print("{0}{1}".format(s1,s2))

#字符串的去重操作‘
s="helloworldhelllldwefsfrsfjsfhhfjhjf"
#字符串的拼接以及not in
new_s=""
for item in s:
    if item not in new_s:
        new_s+=item
print(new_s)

#索引加not in
new_s2=""
for i in range(len(s)):
    if s[i] not in new_s2:
        new_s2+=s[i]
print(new_s2)

#集合去重+列表排序
new_s3=set(s)
lst=list(new_s3)
lst.sort(key=s.index)
print("",join(lst))











