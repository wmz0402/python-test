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





