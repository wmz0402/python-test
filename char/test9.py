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

# #属性的设置
# class Student:
#     def __init__(self,name,gender):
#         self.name = name
#         self.__gender = gender
#
#     #使用@property修改方法，将方法转成属性使用
#     @property
#     def gender(self):
#         return self.__gender
#
# #将我们的gender这个属性设置为可写属性
#     @gender.setter
#     def gender(self,value):
#         if value!="男"and value!="女":
#             print("性别有误，已将性别默认设置为男")
#             self.__gender="男"
#         else:
#             self.__gender=value
#
# stu=Student("陈美美","女")
# print(stu.name,"的性别是：",stu.gender) #stu.gender就是会执行stu.gender()
# stu.gender="其他"
# print(stu.name,"性别是：",stu.gender)
#

# #继承====================================================================
# class Person: #默认继承了object
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show(self):
#         print(f"大家好，我叫：{self.name}，今年{self.age}岁了")
#
# #Student继承Person类·
# class Student(Person):
#     #编写初始化的方法
#     def __init__(self, name, age,stuno):
#         super().__init__(name,age) #调用父类的初始化方法
#         self.stuno = stuno
#
#     #重写
#     def show(self):
#         super().show()    #调用父类的方法
#         print(f"我来自XXX大学，我的学号是：{self.stuno}")
#
# #doctor继承Person
# class Doctor(Person):
#     def __init__(self, name, age,department):
#         super().__init__(name,age)
#         self.department = department
#
# #重写
#     def show(self):
#         # super().show()  也可以不进行调用
#         print(f"我来自XXX医院，我的部门是{self.department}")
#
# #创建第一个子类对象
# stu=Student("陈美美",20,1001)
# stu.show()
# doctor=Doctor("张一一",45,"临床")
# doctor.show()
#
# class FatherA():
#     def __init__(self,name):
#         self.name = name
#
#     def showA(self):
#         print("父类A中的方法")
# class FatherB():
#     def __init__(self,age):
#         self.age = age
#     def showB(self):
#         print("父类B中的方法")
#
# #多继承 继承了多个父类
# class Son(FatherA,FatherB):
#     def __init__(self,name,age,gender):
#         #需要调用两个父类的初始化方法
#         FatherA.__init__(self,name)
#         FatherB.__init__(self,age)
#         self.gender = gender
#
# son=Son("陈美美",20,"女")
# son.showA()
# son.showB()
#
# #多态=====================================================================
# class Person():
#     def eat(self):
#         print("人吃五谷杂粮")
#
# class Cat():
#     def eat(self):
#         print("猫喜欢吃鱼")
# class Dog():
#     def eat(self):
#         print("狗喜欢吃骨头")
# #这三个类中都有一个同名的方法，eat
# #编写函数
# def fun(obj): #obj是函数的形式参数，在定义处不知道数据类型
#     obj.eat()
# #创建三个类对象
# per=Person()
# cat=Cat()
# dog=Dog()
# #调用fun函数
# fun(per)
# fun(cat)
# fun(dog)

# #查看指定对象的属性
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show(self):
#         print(f"大家好，我叫{self.name},我今年{self.age}岁了")
# #创建Person类对象
# per=Person("陈美美",20)
# print(dir(per))


# #__str__方法的重写
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     #方法重写
#     def __str__(self):
#         return "这是个人类，具有name和age两个实例属性"  #返回值是一个字符串
#
# #创建类对象
# per=Person("陈美美",20)
# print(per.__str__())


# # 示例一 计算圆的面积和周长
# class Circle:
#     def __init__(self,r):
#         self.r = r
#
#     #计算面积
#     def get_area(self):
#         return 3.14*self.r*self.r
#     #计算周长
#     def get_perimeter(self):
#         return 3.14*self.r*2
#
# r=eval(input("请输入圆的半径："))
# c=Circle(r)
# print("圆的面积是：",c.get_area())
# print("圆的周长是：",c.get_perimeter())


# #示例二
# class Student:
#     def __init__(self,name,age,gender,score):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.score=score
#     def info(self):
#         print(self.name,self.age,self.gender,self.score)
#
# print("请输入五位学生信息录入：（姓名#年龄#性别#成绩）")
# lst=[]
# for i in range(1,6):
#     s=input(f'请输入第{i}位学生信息及成绩')
#     s_lst=s.split("#")
#     stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])
#     lst.append(stu)
#
# for item in lst:
#     item.info()

# #示例三
# class Instrument():
#     def make_sound(self):
#         pass
#
# class Erhu(Instrument):
#     def make_sound(self):
#         print("二胡在弹奏")
#
# class Pinao(Instrument):
#     def make_sound(self):
#         print("钢琴在弹奏")
#
# class Violin(Instrument):
#     def make_sound(self):
#         print("小提琴在弹奏")
# def play(obj):
#     obj.make_sound()
# er=Erhu()
# vi=Violin()
# pin=Pinao()
# play(er)
# play(vi)
# play(pin)
#

#实战四
class Bike:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand
    def start(self):
        print("启动了")
    def stop(self):
        print("停止了")

class Taxi(Bike):
    def __init__(self,model,brand,company):
        super().__init__(model,brand)
        self.company = company
    def start(self):
        print("乘客你好！")
        print(f"我是{self.company}出租车公司的，我的车牌号是{self.brand}，你要去哪里？")
    def stop(self):
        print("目的地到了，请您扫码付款，欢迎下次乘坐！")
class Car(Bike):
    def __init__(self,model,brand,name):
        super().__init__(model,brand)
        self.name = name
    def start(self):
        print(f"我是{self.name}，我的轿车我做主！")
    def stop(self):
        print("目的地到了，我们去玩吧！")
#测试
taxi=Taxi("广汽丰田","京A8888","长城")
taxi.start()
taxi.stop()
car=Car("上海大众","京B6666","武大郎")
car.start()
car.stop()








