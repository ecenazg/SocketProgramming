import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 5000))

try:
    while True:
        message, addr = server_socket.recvfrom(1024)
        print("Received message:", message.decode())
        print("From:", addr)
except Exception as e:
    print("Server error:", e)
finally:
    server_socket.close()
