import os
import socket

buffer = 2 ** 10
unix_sock = 'unix.sock'
s_sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

if os.path.exists(unix_sock):
    os.remove(unix_sock)

s_sock.bind(unix_sock)

while True:
    try:
        result = s_sock.recv(buffer)
    except KeyboardInterrupt:
        s_sock.close()
    else:
        print('Message from server', result.decode('utf-8'))
