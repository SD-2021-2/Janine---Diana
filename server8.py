import socket

host = '127.0.0.1'  #end do servidor
port = 5005         #porta q o server esta

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # var s - invoca meto socket(ipv4,tcp)
orig = (host, port)
s.bind(orig)   #vinculou rost e porta com o socket

while True:
   #rece msg do cliente
   msgClient = s.recvfrom(1024)
   client = msgClient[1]
   msg = msgClient[0].decode()

   #separa dados da string enviada
   dados = msg.split()
   saldomedio = int(dados[0])
   
   #altera valores de salario
   if saldomedio < 200:
       credito = 0

   elif (saldomedio > 201 and saldomedio < 400):
       credito = 0.2 * saldomedio

   elif (saldomedio > 401 and saldomedio < 600):
       credito = 0.3 * saldomedio
   
   elif saldomedio > 601:
       credito = 0.4 * saldomedio
   
   print(client)
   
   #envia a resposta ao cliente
   s.sendto(credito.encode(), client)



s.close()