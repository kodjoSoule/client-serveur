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
       print(">>>Message de client : ", message_server)
def gestion_client(conn,adrr) :
    print(f'>>>Client : {adrr} connecté')
    connecte = True
    


while True:
    #Ecoutez les connecions entrantes
    server_socket.listen(5)
    #Acceptez la connexion entrante
    conn, address = server_socket.accept()
    
    #Facultative
    #nbre = nbre + 1 
    #print(nbre," client vent de se connecter...")
    gestion_client(conn,address)
    #Recevez des données sur la socket coté serveur
    #data = conn.recv(1024)
    #data = data.decode("utf8")
    #Afficher le message
    #print(data)
    receive_message(conn)
#Fermez la connexion et la socket côté serveur
conn.close()
socket.close()
