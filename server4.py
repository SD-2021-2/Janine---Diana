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
   sexo = dados[0]
   altura = float(dados[1])
  

   #altera valores de salario
   if sexo == 'feminino':
        peso =  float((72.7 * altura) - 58.0)
   elif sexo == 'masculino':
        peso = float((62.1 * altura) - 44.7)

   peso = '%f' % (peso)

   print(client)
   
   #envia a resposta ao cliente
   s.sendto(peso.encode(), client)


s.close()