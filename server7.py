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
   idade = int(dados[1])
   tempo = int(dados[2])
   

   #altera valores de salario
   if idade >= 65:
        texto = 'Pode se aposentar'

   elif idade >= 60:
        if tempo >= 25:
            texto = 'Pode se aposentar'
        else:
            texto = 'Ainda não pode se aposentar'

   print(client)
   print(nome, idade, tempo)
   print(texto)

   #envia a resposta ao cliente
   s.sendto(texto.encode(), client)


s.close()