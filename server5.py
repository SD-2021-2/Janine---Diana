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
   i = int(dados[0])

   if(i >= 5 and i <= 7):
        texto = 'Infantil A'

   elif(i >= 8 and i <= 10):
        texto = 'Infantil B'
    
   elif(i >= 11 and i <= 13):
        texto = 'Juvenil A'
    
   elif(i >= 14 and i <= 17):
        texto = 'Juvenil B'
    
   elif(i >= 18):
        texto = 'Adulto'
    
   else:
        texto = 'Sem categoria'
    
   
   print(client)
   
   
   #envia a resposta ao cliente
   s.sendto(texto.encode(), client)


s.close()