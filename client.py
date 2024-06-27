import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("Hola, servidor".encode(), ('127.0.0.1', 12345))
response, server = s.recvfrom(1024)
print(response.decode())

