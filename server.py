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
def receive_message(conn):
    message_server = conn.recv(1024).decode("utf8")
    global isConnected
    if not message_server :
        print("LE client est deconnecté ")
        isConnected = False
    else:
        print(">>>Message de client : ", message_server)
def gestion_client(clien,adrr) :
    global nbre 
    nbre += 1
    print(f'>>>{nbre} client : {adrr} connecté')
    connecte = True
    


while True:
    isConnected = True
    #Ecoutez les connecions entrantes
    server_socket.listen(5)
    print("En ecoute")
    #Acceptez la connexion entrante
    #conn, address = server_socket.accept()
    client_socket, client_address = server_socket.accept()
    
    #Facultative
    #nbre = nbre + 1 
    #print(nbre," client vent de se connecter...")
    gestion_client(client_socket,client_address)
    #Recevez des données sur la socket coté serveur
    #data = conn.recv(1024)
    #data = data.decode("utf8")
    #Afficher le message
    #print(data)
    while True :
        receive_message(client_socket)
        if not isConnected :
            break
#Fermez la connexion et la socket côté serveur
conn.close()
socket.close()
