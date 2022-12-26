#coding:utf-8
import socket
import threading        
host, port = ('localhost', 5050)
TAILLE = 1024
FORMAT = "utf8"
#Creer une socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Liez la socket a une adresse et un port
server_socket.bind((host, port))
print(">>>Le serveur est demarrer ...")
nbre = 0 
#Ecoutez les connecions entrantes
server_socket.listen(5)
print("En ecoute")

#Declaration des fonction

def gerer_client(client,adrr) :
    print(f'>>> {adrr} client : connecté')
    while True :
        message_server = client.recv(1024).decode("utf8")
        if not message_server :
            print(f"Le client {adrr}est deconnecté ")
            break
        else:
            print("[\n Message recu de  {} client : {}".format(adrr, message_server))
            print("\n]")

#FIN Declaration des fonction
while True:
    #Acceptez la connexion entrante
    #conn, address = server_socket.accept()
    client_socket, client_address = server_socket.accept()
    
     #création d'un thread pour gérer la connexion client
    thread = threading.Thread(target=gerer_client,args=(client_socket,client_address))
    thread.start()

#Fermez la connexion et la socket côté serveur
conn.close()
socket.close()
