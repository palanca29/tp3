import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.2.6.106',12345))

s.listen()
print("esperando conexion")
conn, addr = s.accept()

data = conn.recv(1024)   

conn.sendall("Message for client".encode())

print(data)
