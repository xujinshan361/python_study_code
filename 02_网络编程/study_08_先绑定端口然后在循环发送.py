import socket


def main():
    # 创建第一个upd套接字
    upd_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定本地信息
    upd_socket.bind("", 6783)
    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")
        # 可以使用套接字收发送数据
        # upd_socket.sendto("helllo",对方的ip以及对方的port)
        # upd_socket.sendto(b"hello-----------1--------------", ("192.168.56.1", 8080))        # 发送的数据必须是bytes类型
        upd_socket.sendto(send_data.encode("utf-8"), ("192.168.56.1", 8080))  # 设置编码格式为utf-8，可以进行发送

    # 关闭套接字
    upd_socket.close()
