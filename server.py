from http import client
import socket

server_ip = '127.0.0.1'
port = 9999

# 서버 소켓 주비
server = socket.socket()

server.bind((server_ip, port))
server.listen(1)
print('---- Server is ready ----')

# 클라이언트 접속 수락
client, adder = server.accept()
print('---- Client is connected ----')

# 메시지 수신
msg = client.recv(1024)
print('---- Message received ----')
print(msg)

# 메시지 송신
client.send(b'Hi Hi i\'m server.You\'re name is : ' + msg)
print('---- Message send ----')

# 해제
client.close()
server.close()