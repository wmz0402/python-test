# #类的组成
# class Student:
#     #类属性：定义在类中，方法外的变量
#     school="北京XXX教育"
#     #初始方法的方法
#     def __init__(self,xm,age):
#         self.name=xm  #=左侧是实例属性，xm是局部变量，将局部变量的值xm赋值给实例属性self.name
#         self.age=age  #实例的名称和局部变量的名称可以相同
#     # 定义在类中的函数，称为方法，自带一个参数self
#     def show(self):
#         print(f'我叫{self.name},今年：{self.age}岁了')
#
#     #静态方法
#     @staticmethod
#     def sm():
#         print("这是一个静态方法，不能调用实例属性，也不能调用实例方法")
#
#     #类方法
#     @classmethod
#     def cm(cls): #cls-->class的缩写
#         print("这是一个类方法，不能调用实例属性，也不能调用实例方法")
#
# #创建类的对象
# stu=Student("wmz",18) #为什么传两个参数，因为————init————方法中有两个形参，self，是自带的参数，无需手动传入
# #实例属性，使用对象名进行打点调用的
# print(stu.name)
# print(stu.age)
# #类属性，直接使用类名打点调用
# print(Student.school)
#
# #实例方法，使用对象名进行打点调用
# stu.show()
# #类方法，@classmethod进行修饰的方法，直接使用类名打点调用
# Student.cm()
# #静态方法@staticmethod进行修饰的方法，直接使用类名打点调用
# Student.sm()

# #编写学生类，并创建四个学生对象
# class Student:
#     school="北京XXX教育"
#     def __init__(self,xm,age):
#         self.name=xm
#         self.age=age
#     def show(self):
#         print(f"我叫{self.name},今年{self.age}岁了")
#
# stu=Student("wmz",18)
# stu2=Student("陈梅梅",20)
# stu3=Student("玛丽",21)
# stu4=Student("Marry",23)
# print(type(stu))
#
# Student.school="梅西教育"   #给类的类属性赋值
# lst=[stu,stu2,stu3,stu4]
# for item in lst:
#     item.show()
#
#
# #动态绑定属性和方法
# #为stu2绑定一个实例属性
# stu2.gender="男"
# print(stu2.name,stu2.age,stu2.gender)
# #动态绑定方法
# def introduce():
#     print("我是一个普通的函数，我被动态绑定成stu2对象的方法")
# stu2.fun=introduce #函数的一个赋值
# #fun就是stu2对象的方法
# #调用
# stu2.fun()
#

# #权限控制
# class Student():
#     #首尾双下划线
#     def __init__(self,name,age,gender):
#         self._name=name #self._name受保护的只能本类和子类访问
#         self.__age=age #self.__age表示私有，只能类本身去访问
#         self.gender=gender #普通的实例属性，类的内部，外部，级子类都可以访问
#
#     def _fun1(self):  #受保护的
#         print("子类即本身可以访问")
#
#     def __fun2(self):#私有
#         print("只有定义的类可以访问")
#
#     def show(self):  #普通的实例方法
#         self._fun1()  #类本身访问受保护的方法
#         self.__fun2()  #类本身访问私有方法
#         print(self._name)  #受保护的实例属性
#         print(self.__age)  #私有的实例属性
#
# #创建一个学生类对象
# stu=Student("陈美美",20,"女")
# #类的外部
# print(stu._name)
# #调用受保护的实例方法
# stu._fun1() #子类即本身可以访问
# #私有方法
# #stu.__fun2()     报错
# #正确访问私有方法
# print(stu._Student__age)
# stu._Student__fun2()

#属性的设置
class Student:
    def __init__(self,name,gender):
        self.name = name
        self.__gender = gender

    #使用@property修改方法，将方法转成属性使用
    @property
    def gender(self):
        return self.__gender

#将我们的gender这个属性设置为可写属性
    @gender.setter
    def gender(self,value):
        if value!="男"and value!="女":
            print("性别有误，已将性别默认设置为男")
            self.__gender="男"
        else:
            self.__gender=value

stu=Student("陈美美","女")
print(stu.name,"的性别是：",stu.gender) #stu.gender就是会执行stu.gender()
stu.gender="其他"
print(stu.name,"性别是：",stu.gender)




