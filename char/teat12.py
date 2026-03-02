#服务器端代码编写
from socket import socket, AF_INET,SOCK_STREAM
#AF_INET 用于Internet之间的进程监听
#SOCK_STREAM 表示的是用TCP协议程序

#创建socket对象
server_socket = socket(AF_INET, SOCK_STREAM)
#绑定IP地址和端口
ip="127.0.0.1" #等同于local
port=8888 #端口范围
server_socket.bind((ip, port))

#使用listen（）开始监听
server_socket.listen(5)
print("服务器已启动")

#等待客户端连接
client_socket, client_addr = server_socket.accept()

#接收来自客户端的数据
date=client_socket.recv(1024)
print("客户端发来的数据是：",date.decode())

#关闭scoket
server_socket.close()