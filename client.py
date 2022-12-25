#coding:utf-8
import socket
FORMAT = 'utf-8'
TAILLE = 1024
PORT = 5050
#host, port = ('localhost', 5050)
host, port = ('localhost', 5050)
#Creer une socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def send_message(message):
    message = message.encode("utf8")
    client_socket.sendall(message)


try:
    #Connecterz la socket au serveur
    client_socket.connect((host, port))
    print(">>>Client connecté !")
    ##Envoie de message 
    data = "Bonjour a toi, je suis le client !"
    #data = data.encode("utf8")
    send_message(data)
    #Envoyez des données sur la socket coté client
    #client_socket.sendall(data)
except :
    print(">>>Connecton au serveur echouée ! ")
finally:
    client_socket.close()