import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 12345))
print("esperando mensaje")
data, addr = s.recvfrom(1024)
s.sendto("Message for client".encode(), addr)
print(data.decode())


