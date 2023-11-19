import socket
import json

# 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定IP和端口
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(1)
print('服务器正在监听端口 {} ...'.format(server_address[1]))

while True:
    # 等待客户端连接
    print('等待客户端连接...')
    client_socket, client_address = server_socket.accept()
    print('客户端已连接：{}'.format(client_address))

    try:
        while True:
            # 接收客户端请求
            data = client_socket.recv(1024)
            if not data:
                break

            # 解析客户端请求
            request = json.loads(data.decode('utf-8'))
            action = request.get('action')

            # 处理不同请求
            if action == 'view':
                # 从存储中读取联系人信息
                # 在实际应用中，这里可以连接数据库进行查询
                # 这里简化为一个示例
                response = {'contacts': [{'name': 'John', 'address': '123 Main St', 'phone': '555-1234'},
                                          {'name': 'Alice', 'address': '456 Oak St', 'phone': '555-5678'}]}
            elif action == 'add':
                # 添加联系人
                # 在实际应用中，这里可以连接数据库进行插入
                # 这里简化为一个示例
                new_contact = request.get('contact')
                response = {'message': 'Contact added successfully.'}
            elif action == 'update':
                # 更新联系人
                # 在实际应用中，这里可以连接数据库进行更新
                # 这里简化为一个示例
                updated_contact = request.get('contact')
                response = {'message': 'Contact updated successfully.'}
            elif action == 'delete':
                # 删除联系人
                # 在实际应用中，这里可以连接数据库进行删除
                # 这里简化为一个示例
                contact_to_delete = request.get('contact')
                response = {'message': 'Contact deleted successfully.'}
            else:
                response = {'error': 'Invalid action'}

            # 将响应发送给客户端
            response_json = json.dumps(response)
            client_socket.send(response_json.encode('utf-8'))

    finally:
        # 关闭连接
        print('与客户端断开连接...')
        client_socket.close()
