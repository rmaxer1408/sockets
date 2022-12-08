import socket

HOST = '127.0.0.1'
PORT = 8888
buff = 2 ** 10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(4)
# sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# sock.setblocking(False) -> sock.settimeout(0)
# sock.setblocking(True) -> sock.settimeout(None)
sock.settimeout(5)

while True:
    try:
        c_sock, addr = sock.accept()
    except socket.error:
        print('no clients')
    # except socket.timeout:
    #     print('timed out')
    except KeyboardInterrupt:
        print('stopped server')
        break
    else:
        c_sock.setblocking(True)
        result = c_sock.recv(buff)
        c_sock.close()
        print('Message from server', result.decode('utf-8'))
