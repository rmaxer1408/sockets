import socket


HOST = '127.0.0.1'
PORT = 8888
message = b'Message to server'

client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.sendto(message, (HOST, PORT))
