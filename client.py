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
def receive_message(conn):
       message_server = conn.recv(1024).decode("utf8")
       return message_server
       ##cd Desktop\Python\client_serveur

try:
    #Connecterz la socket au serveur
    client_socket.connect((host, port))
    print(">>>Client connecté !")
    ##Envoie de message 
    data = "Bonjour a toi, je suis le client !"
    #data = data.encode("utf8")
    
    
    ###send_message(data)
    
    
    #Envoyez des données sur la socket coté client
    #client_socket.sendall(data)
    #if __name__ == "___main___":
    while True :
        text = input("Merci de siaisr votre prenom : ")
        send_message(text)
        print("1__Oui")
        print("2__Non")
        verifie = int(input(">\:"))
        if verifie == 2 :
            break
        #message_server = receive_message(client_socket)
        #print(">>> MSG : ", message_server)
except :
    print(">>>Connecton au serveur echouée ! ")
#finally:
#    client_socket.close()











