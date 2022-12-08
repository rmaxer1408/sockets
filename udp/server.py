import socket

HOST = '127.0.0.1'
PORT = 8888
buffer = 2 ** 10
message_s = 'Message'

server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind((HOST, PORT))

while True:
    try:
        result = server_sock.recv(buffer)
    except KeyboardInterrupt:
        server_sock.close()
        break
    else:
        print(message_s, result.decode('utf-8'))
