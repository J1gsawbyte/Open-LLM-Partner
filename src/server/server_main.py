# main.py
import requests
import json
import socket
import sys

def start_server(host='127.0.0.1', port = 65432):
    # 创建一个 socket 对象
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # 绑定地址和端口
        server_socket.bind((host, 65432))
        # 监听
        server_socket.listen()
        print(f"服务器正在监听 {host}:65432")
        # 接受客户端连接
        conn, addr = server_socket.accept()
        with conn:
            print(f"已连接 {addr}")
            while True:
                # 接收客户端发送的数据
                data = conn.recv(1024)
                if not data:
                    break
                print(f"收到来自客户端的消息: {data.decode('utf-8')}")
                # 从终端读取用户输入
                message = input("请输入消息: ")
                # 发送消息给客户端
                conn.sendall(message.encode('utf-8'))
                if message == 'exit':
                    break

if __name__ == "__main__":
    start_server()

def ResponseFromAI(message):
    json_data = {
      'message': message,
      'mode':'chat',
    }
    headers = {
      'Content-Type':'application/json',
      'Authorization': 'Bearer 3WC2FYH-KC74W8B-HAY5Q11-8G3W33D',
      'accept':'application/json'
    }
    response = requests.post('http://localhost:3001/api/v1/workspace/test/chat', headers=headers ,json=json_data)
    answer_dict = json.loads(response.content)
    # answer_dict已经拿到了AI返回的结果了，以下两行是去除掉输出的思考过程
    answer = answer_dict['textResponse'].__str__()
    final_answer = answer[answer.index('</think>')+len('</think>')+1:]
    return final_answer
