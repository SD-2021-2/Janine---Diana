import socket

host = '127.0.0.1'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
dest = (host, port)

msg = input('Informe sexo e altura\n')

#envia msg para servidor
s.sendto(msg.encode(), dest)

#recebe resposta
data, server = s.recvfrom(1024)

print(data.decode())

s.close()