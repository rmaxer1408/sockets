import socket

c_sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
c_sock.sendto(b'Message to server', 'unix.sock')
