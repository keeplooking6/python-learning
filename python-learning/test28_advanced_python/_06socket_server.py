import socket
# 创建socket对象
socket_server = socket.socket()
# 绑定socket_server到指定地址和ip
socket_server.bind(("127.0.0.1",8888))
# 服务器开始监听端口
socket_server.listen(8888)
# 接受客户端链接，获得连接对象,没有消息就阻塞在这里，conn是服务器和客户端连接的对象
conn,address = socket_server.accept()
print(f"服务端连接到来自{address}的客户端")
# 连接成功后，recv方法接收客户端信息
while True:
    # recv是阻塞式的，等不到消息就一直卡着
    data: str = conn.recv(1024).decode("UTF-8")
    # recv返回的是字节数组，通过decode方法解码为字符串
#     rece的参数为缓冲区大小（buffsize）
    print(f"接收的数据：{data}")
    if data == 'exit':
        print("客户端已断开")
        break

    msg: str = input("请输入发给客户端的消息：")
    conn.send(msg.encode("UTF-8"))
    if msg == 'exit':
        break

# 关闭连接
conn.close()
socket_server.close()
