import socket

HOST = '127.0.0.1'
PORT = 8888
buff = 2 ** 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(4)

while True:
    try:
        c_sock, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = c_sock.recv(buff)
        c_sock.close()
        print('Message from server', result.decode('utf-8'))
