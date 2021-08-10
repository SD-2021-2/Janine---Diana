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
   nome = dados[0]
   nivel = dados[1]
   salario = float(dados[2])
   depen = int(dados[3])
   

   #altera valores de salario
   if nivel == 'A':
        if depen == 0:
            salario += salario * 0.03
        else:
            salario += salario * 0.08

   elif nivel == 'B':
        if depen == 0:
            salario += salario * 0.05
        else:
            salario += salario * 0.10

   elif nivel == 'C':
        if depen == 0:
            salario += salario * 0.08
        else:
            salario += salario * 0.15

   elif nivel == 'D':
        if depen == 0:
            salario += salario * 0.10
        else:
            salario += salario * 0.17



   #formata a string de resosta
   texto = '%s %f %s' % (nome, salario, nivel)
   
   print(client)
   print(nome, salario, nivel)
   
   #envia a resposta ao cliente
   s.sendto(texto.encode(), client)


s.close()