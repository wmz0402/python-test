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











