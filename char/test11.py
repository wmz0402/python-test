
# #文件的读写操作
# def my_write():
#     #打开或创建文件
#     file=open("a.txt","w",encoding="utf-8")
#     #操作文件
#     file.write("伟大的中国梦")
#     #关闭
#     file.close()
# #读取
# def my_read():
#     #创建打开文件
#     file=open("a.txt","r",encoding="utf-8")
#     #操作文件
#     s=file.read()
#     print(type(s),s)
#     #关闭文件
#     file.close()
#
# #主程序运行
# if __name__ == '__main__':
#     my_write()
#     my_read()

# #文件的写入操作---------------------------------------------------
# def my_write(s):
#     file=open("b.txt","a",encoding="utf-8")
#     file.write(s)
#     file.write("\n")
#     file.close()
#
# def my_write_list(file,lst):
#     f=open(file,"a",encoding="utf-8")
#     f.writelines(lst)
#     f.close()
#
# if __name__ == '__main__':
#     # my_write("伟大的中国梦")
#     # my_write("北京欢迎你")
#     #准备数据
#     lst=["姓名\t","年龄\t","成绩\n","张三\t","30\t","98"]
#     my_write_list("c.txt",lst)


# #文件的读取操作-------------------------------------------------
# def my_read(filename):
#     #打开
#     file=open(filename,"w+",encoding="utf-8")
#     #操作
#     file.write("你好啊")#写入完成，文件指针在最后
#     #seek 修改文件指针位置
#     file.seek(0)
#     #读取
#     # s=file.read()#读取全部
#     # s=file.read(2) #读取两个字符
#     # s=file.readline() #读取一行数据
#     # s=file.readline(2) #读取一行中的两个字符
#     # s=file.readlines() #读取所有，一行为列表中的一个元素，s是列表类型
#     #读取好啊
#     file.seek(3) #在utf-8中一个中文字符占3个字节
#     s=file.read()
#     print(type(s),s)
#
#     #关闭
#     file.close()
#
# if __name__ == '__main__':
#     my_read("d.txt")
#
# #文件的复制==================================================
# def copy(src,new_path):
#     #文件的复制就是边读边写的操作
#     #打开源文件
#     file1=open(src,"rb")
#     #打开目标文件
#     file2=open(new_path,"wb")
#     #开始复制边读边写
#     s=file1.read() #源文件读取操作
#     file2.write(s)#目标文件写入操作
#
#     #关闭
#     file2.close()
#     file1.close() #先打开的后关，后打开的先关
#
# if __name__ == '__main__':
#     src="./iphone1.jpg"
#     new_path="./iphone2.jpg"
#     copy(src,new_path)
#



