import socket


def main():
    # 1 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2 绑定一个本地信息
    localaddr = ('192.168.56.1', 8899)
    udp_socket.bind(localaddr)  # 必须绑定自己的信息，其他电脑不行
    # 3 接收数据
    recv_data = udp_socket.recvfrom(1024)
    # recv_data 这个变量接收到的数据是一个元组 (接收到的数据,(发送方ip,发送方端口号))
    recv_message = recv_data[0]  # 存储接收到的数据
    rece_addr = recv_data[1]  # 存储发送方的地址信息
    # 4 打印接收到的数据
    print("{0} : {1}".format(rece_addr, recv_message.decode("gbk")))
    # 5 关闭套接字
    udp_socket.close()


if __name__ == "main()":
    main()
