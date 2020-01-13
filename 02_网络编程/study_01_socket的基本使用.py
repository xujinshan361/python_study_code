import socket


def main():
    # 创建第一个upd套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发送数据
    # upd_socket.sendto("helllo",对方的ip以及对方的port)
    upd_socket.sendto(b"hello-----------1--------------", ("192.168.56.1", 8080))

    # 关闭套接字
    upd_socket.close()


if __name__ == "__main__":
    main()
