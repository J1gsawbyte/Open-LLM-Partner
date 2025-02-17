#使用socket写一个客户端
# # client.py
import socket
import sys

def start_client(host='119.84.246.217',port = 29791):
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 连接服务器
        client_socket.connect((host, port))
        print(f"已连接服务器 {host}:65432")
        while True:
            # 从终端读取用户输入
            message = input("请输入消息: ")
            # 发送消息给服务器
            client_socket.sendall(message.encode('utf-8'))
            # 接收服务器发送的数据
            data = client_socket.recv(1024)
            print(f"收到来自服务器的消息: {data.decode('utf-8')}")
            if message == 'exit':
                break

if __name__ == "__main__":
    start_client()