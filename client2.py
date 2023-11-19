import socket
import json

# 创建socket对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务器
server_address = ('localhost', 12345)
client_socket.connect(server_address)

while True:
    # 用户输入操作
    action = input('请输入操作（view/add/update/delete/exit）: ')

    if action == 'exit':
        break

    # 构建请求
    request = {'action': action}

    if action == 'add' or action == 'update':
        # 添加或更新联系人时，需要提供联系人信息
        name = input('请输入姓名: ')
        address = input('请输入住址: ')
        phone = input('请输入电话: ')
        request['contact'] = {'name': name, 'address': address, 'phone': phone}

    # 将请求发送给服务器
    request_json = json.dumps(request)
    client_socket.send(request_json.encode('utf-8'))

    # 接收服务器响应
    response_json = client_socket.recv(1024)
    response = json.loads(response_json.decode('utf-8'))

    # 处理服务器响应
    print(response)

# 关闭连接
client_socket.close()
