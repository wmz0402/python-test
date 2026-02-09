#序列的切片操作
s="HelloWorld"
s1=s[0:5:2] #索引从零开始到五结束（不包含五）步长为2
print(s1)
#省略了开始位置，start默认从0开始
#省略步长stop默认为1
print(s[:5:2])
print(s[:5:])
#结束位置没写默认到序列的末尾
print(s[0::1])

#字符串的一些用法
ss="helloworld"
print('h' in ss)
print('v' in ss)
print('w' not in ss)
print('v' not in ss)
print("ss中最大的",max(ss))
print(min(ss))
print(len(ss))
print("第一次出现的索引：",ss.index('o'))
print("出现的次数：",ss.count('o'))

lst = ["hello","world","python"]
print("源列表",lst,id(lst)) #打印源列表以及源列表的地址
#增加元素
lst.append("asd")
print("增加元素后的列表",lst,id(lst))
#使用insert(index,x)在指定index位置上插入元素x
lst.insert(1,100)
print("插入元素后的列表",lst,id(lst))
#列表元素的删除操作
lst.remove("asd")
print("删除后的链表",lst,id(lst))
#pop实现取出再删除
print(lst.pop(1))
print(lst)
#列表反向
lst.reverse()
print(lst,id(lst))
#列表的拷贝操作
new_lst=lst.copy()
print("新生成的列表",new_lst,id(new_lst))
#列表的修改操作
lst[1]="myscore"
print(lst,id(lst))
#清空列表中的所有元素
lst.clear()
print("清空后的列表",lst,id(lst))

print("-----------------------------------------------------")
#列表的排序操作
lst1=[56,2,36,45,66,89,68,35,23,46]
print("源列表",lst1)
#默认排序 升序
lst1.sort()
print("排序好的列表",lst1)
#降序排序
lst1.sort(reverse=True)
print(lst1)


print("=========================================================")
#对字符进行排序
lst2=["apple","Cat","Orange","banana"]
#默认排序，先排大写再排小写
lst2.sort()
print(lst2)
#降序排列
lst2.sort(reverse=True)
print(lst2)
#忽略大小写进行排序
lst2.sort(key=str.lower)
print(lst2)

print("=============================================")
#内置排序函数
lst3=[33,65,36,96,89,56,4,43,65,98]
print(lst3)
#产生一个新的列表，源列表并不会发生任何改变
asc_lst=sorted(lst3)  #默认排序升序
print(asc_lst)
#降序排列
desc_lst=sorted(lst3,reverse=True)
print(desc_lst)

print("========================================")
#列表生成式
import random
lst4=[item for item in range(1,11)]
print(lst4)
lst4=[item*item for item in range(1,11)]
print(lst4)
lst4=[random.randint(1,100) for _ in range(10)]
print(lst4)
#在列表中选择符合条件的数组成列表
lst4=[item for item in range(10) if item%2==0]
print(lst4)

print("===========================================")
#二维列表的创建和便利
lst=[
    ["城市","环比","同比"],
    ["北京",102,103],
    ["上海",104,504],
    ["深圳",100,39]
]
print(lst)
#遍历二维列表通常使用双层for循环
for row in lst:
    for item in row:
        print(item,end="\t")
    print()

# 列表生成一个4行5列的二维列表
lst2 =[ [j for j in range(5)]for i in range(4)]
print(lst2)

# 元组
#如果元组中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))
t=('hello',[1,2,3,4,5,6],'world')
print(t,type(t))
t=tuple("helloworld")
print(t)
t=([10,20,30,40,50,60,70,80,90,100])
print(t)
print(10 in t)
print(10 not in t)
print(max(t))
print(min(t))
print(len(t))
print(t.count(10))
print(t.index(10))

del t#元组的删除

m=("pythen","hello","world")
# 根据索引访问元素
print(m[0])
t2=m[0:3:2]
print(t2)
# 元组遍历
for item in m:
    print(item)

#for+range()+len()
for i in range(len(m)):
    print(i,m[i])

for index,item in enumerate(m,start=11):#可以规定开始的序列
    print(index,"-------------->",item)

#元组生成式
t3=(i for i in range(1,4))
print(t3)

print(t3.__next__())#取出第一个元素
print(t3.__next__())#取出第二个元素
print(t3.__next__())#取出最后·一个元素 已经没有元素了
t3=tuple(t3)
print(t3)

for item in t3:
    print(item)

#字典 键值对 不可变序列
#创建字典
d={10:"cat",20:"dog",30:"pet",20:"zoo"}
print(d) #key值相同时，value值进行了覆盖
#zip函数
lst1=[10,20,30,40]
lst2=["cat","dog","pet","zoo","car"]
zipobj=zip(lst1,lst2)
print(zipobj)
#print(list(zipobj))
d=dict(zipobj)
print(d)

#使用参数创建字典
d=dict(cat=10,dog=20)
print(d)

t=(10,20,30)
print({t:10})  #元组可以作为字典中的key

#可变数据类型不能作为字典当中的键 列表不能作为字典当中的键
print(max(d))
print(min(d))
print(len(d))#长度为个数5
del d #字典的删除

#字典元素的访问和遍历
d={"hello":10,"world":20,"python":30}
#访问字典中的元素
print(d["hello"])
#d.get(key)
print(d.get("python"))

#当key不存在时d[key]报错d.get(key)可以指定默认值
#print(d["java"])
print(d.get("java"))
print(d.get("java","不存在"))

#字典的遍历
for item in d.items():
    print(item) #key=value组成一个元素

#使用for循环遍历时，分别获取key,value
for key,value in d.items():
    print(key,value)

#字典的相关操作方法
d={1001:"李梅",1002:"王华",1003:"张锋"}
print(d)
#像字典中添加元素
d[1004]="张丽丽"
print(d)

#获取字典中所有的key
keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))
#获取字典中所有的value
values=d.values()
print(values)

#如何将字典中的数据转换成键值对的形式key-value的形式，以元组的方式进行展现
lst=list(d.items())
print(lst)
d=dict(lst)
print(d)

#使用pop函数  删除元素
print(d.pop(1001))
print(d)
#可以设置默认值
print(d.pop(1008,"不存在"))
print(d)

#随机删除
print(d.popitem())
print(d)

#清空字典中的所有元素
d.clear()
print(d)

#字典的生成式
import random
#生成随机数
d={item:random.randint(1,100) for item in range(4)}
print(d)

#创建两个列表
lst=[1001,1002,1003]
lst2=["陈美美","王一一","李丽丽"]
d={key:value for key,value in zip(lst,lst2)}
print(d)

#集合类型 1.是一个无限的不重复元素序列2.只能存储不可变数据类型
#使用{}直接创建
s={10,20,30}
print(s)
#集合只能存储不可变数据类型
#s={[10,20],[30,40]}
print(s)

#使用set创建
s=set()
print(s)
s={}  #字典类型不是集合
print(s,type(s))
#集合是无序不重复
s=set("helloworld")
print(s)

s2=set([10,20,30])
print(s2)

s3=set(range(1,10))
print(s3)

#集合属于序列的一中
print(max(s3))
print(min(s3))
print(len(s3))
print(9 in s3)
print(9 not in s3)

del s3
#print(s3)

A={10,20,30,40,50}
B={30,40,88,67,20}
#交集操作
print(A&B)
#并集
print(A|B)
#差集
print(A-B)
#补集
print(A^B)

s={10,20,30}
#向集合当中添加元素
s.add(100)
print(s)
#删除元素
s.remove(100)
print(s)
#清空元素
# s.clear()
# print(s)

#集合的遍历操作
for item in s:
    print(item)

for index,item in enumerate(s):  #序号
    print(index,item)

#集合生成式
s={i for i in range(1,10)}
print(s)

s={i for i in range(1,10) if i%2==0}
print(s)

#结构的数据匹配
date=eval(input("请输入要匹配的数据："))
match date:
    case {"name":"ysj","age":20}:
        print("字典")
    case [10,20,30]:
        print("列表")
    case (10,20,40):
        print("元组")
    case _:
        print("相当于else")

#合并字典的操作
d1={"a":10,"b":20}
d2={"c":30,"d":40,"e":50}
merged_dict=d1|d2
print(merged_dict)

#同步迭代
fruits=["apple","orange","banana","mango"]
counts=[10,3,4,5]
for f,c in zip(fruits,counts):
    match f,c:
        case "apple",10:
            print("apple")
        case "orange",3:
            print("orange")
        case "banana",4:
            print("banana")
        case "mango",5:
            print("mango")





























