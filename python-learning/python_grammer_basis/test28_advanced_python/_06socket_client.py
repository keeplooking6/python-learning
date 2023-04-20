import socket
# 创建对象
socket_client = socket.socket()
# 连接到服务端
socket_client.connect(("localhost",8888))
# 发送消息
while True:
    send_msg = input("请输入要发送的信息：")
    socket_client.send(send_msg.encode("UTF-8"))
    if send_msg == 'exit':
        break

    # recv是阻塞式的，等不到消息就一直卡着
    recv_data = socket_client.recv(1024)
    msg = recv_data.decode("UTF-8")
    if msg == 'exit':
        print("服务端已断开")
        break
    print("服务端回复消息为：",msg)
socket_client.close()
