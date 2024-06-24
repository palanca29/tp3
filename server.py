import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',12345))

s.listen()
print("esperando conexion")
conn, addr = s.accept()

data, addr = s.recv(1024)   

s.sendall("Message for client".encode())

print("hola")
print(data)

s.close()