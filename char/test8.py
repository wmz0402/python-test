#可变参数的使用
#一颗星个数可变的位置传参
def fun(*para):
    print(type(para))
    for item in para:
        print(item)

#调用
fun(1,2,3,4,5)
fun([11,22,33,44])
#在调用时，参数前加一颗星，会将列表进行解包
fun(*[11,22,33,44])

#个数可变的关键字参数
def fun2(**kwpara):
    print(type(kwpara))
    for key,value in kwpara.items():
        print(key,"------>",value)
fun2(name="ysj",age=18,height=170)


d={"name":"ysj","age":18,"height":170}
#如果参数是字典前面必须加上两颗星进行系列解包操作
fun2(**d)

#匿名函数的使用
s=lambda a,b:a+b #s表示一个匿名函数
print(type(s))
#调用匿名函数
print(s(10,20))
print("-"*30)
#列表的取值
#正常情况
lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])
print("-"*30)
for i in range(len(lst)):
    result=lambda x:x[i] #根据素银取值，result的类型是function，x是形式参数
    print(result(lst)) #lst是实际参数
print("-"*30)

student_score=[
    {"name":"陈美美","score":98},
    {"name":"王一一","score":95},
    {"name":"张天了","score":85},
    {"name":"白雪而","score":65},
]
#对列表进行排序，依据成绩进行排序
student_score.sort(key=lambda  x:x.get("score"), reverse=True) #按成绩降序进行排列
print(student_score)
print("-"*30)

#递归操作
def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(5))
print("-"*30)

#斐波那契额数列
def face(n):
    if n==1 or n==2:
        return 1
    else:
        return face(n-1)+face(n-2)
print(face(9))
print("-"*30)

#迭代器操作
lst=[54,56,32,69,89,72]
asc_lst=sorted(lst)
desc_lst=sorted(lst,reverse=True)
print(asc_lst)    #默认升序
print(desc_lst)   #降序
print("-"*30)
#reverse
new_lst=reversed(lst)
print(new_lst)     #他的对象是一个迭代器
print(list(new_lst))   #转化成列表才能正常的输出
print("-"*30)
#zip操作
x=['a','b','c','d']
y=[10,20,30,40,50]
zipobj=zip(x,y)
print(type(zipobj))
# print(list(zipobj))
print("-"*30)
#enumerate
enum=enumerate(y,1)
print(type(enum))
print(list(enum))
print("-"*30)
#all
lat2=[10,20,'',30]
print(all(lat2))
print(all(lst))
print("-"*30)
print(any(lst))
print(any(lat2))   #所有元素都为false结果才为false
print("-"*30)
#next
print(next(zipobj))
print(next(zipobj))
print(next(zipobj)) #每运行一次就会遍历一个元素

#filter
def fun(num):
    return num%2==1 #可能是·false也可能是true
obj=filter(fun,range(10))  #将range（10），0-9的整数，都执行一次fun操作
print(list(obj))#留下结果为true的
print("-"*30)

#map
def upper(x):
    return x.upper()
new_lst2=["hello","world","python"]
obj2=map(upper,new_lst2)
print(list(obj2))
print("-"*30)


#format()内置函数
print(format(3.14,'20'))  #数值默认右对齐
print("hello","20")  #字符串默认左对齐
print("hello","*<20")  #*表示填充符，<表示左对齐，20表示宽度
print(format(3.14,'.2f'))
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))
print("-"*30)

#找寻列表中的最大值
import random
def get_max(lst):
    x=lst[0]
    for i in range (1,len(lst)):
        if x<lst[i]:
            x=lst[i]
    return x
lst=[random.randint(1,100) for item in range(10)]
print(lst)
max=get_max(lst)
print(max)
print("-"*30)
def get_max2(lst):
    sorted_lst=sorted(lst,reverse=True)
    return sorted_lst[0]
lst=[random.randint(1,100) for item in range(10)]
print(lst)
max=get_max2(lst)
print(max)
print("-"*30)

def getu
















