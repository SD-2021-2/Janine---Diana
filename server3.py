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
   N1 = int(dados[0])
   N2 = int(dados[1])
   N3 = int(dados[2])
   
   M = float((N1 + N2 ) / 2 )
   #altera valores de salario
   if M >= 7.0:
        texto = 'Aprovado'

   elif M >= 3.0 and M <= 7.0:
        texto = 'Aluno deve refazer'
        if (M + N3 / 2) >= 7.0:
            texto = 'Aprovado'
        else:
            texto = 'Reprovado'
   
   print(client)
   print(texto)
   
   #envia a resposta ao cliente
   s.sendto(texto.encode(), client)


s.close()