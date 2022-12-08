import socket

HOST = ''
PORT = 8888

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST, PORT))
    sock.send(b'Hello')
except socket.error:
    print('Oops..')
sock.close()
