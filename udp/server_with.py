import socket

HOST = '127.0.0.1'
PORT = 8888

# __enter__/__exit__
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f'{PORT} was bind')

    while True:
        result = sock.recv(2 ** 10)
        print('Message from server', result.decode('utf-8'))
